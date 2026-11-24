#!/usr/bin/env python3
"""Build an interactive LL.B study book (single HTML file) from a plain-text content file.

Content format (one directive per line):
  @title / @subtitle / @paper / @sem / @color / @dark / @intro / @reading  (book meta)
  # N | Chapter title          start a unit
  @topics a; b; c              syllabus topics for the unit
  >> text                      unit thesis line
  ## heading / ### subheading
  - bullet / 1. numbered
  SEC: label :: text           statute box
  CASE: name (year) :: text    case box (goes to case index)
  NOTE: text                   current-law note
  TIP: text                    exam tip
  |a|b|c|                      table row (first row = header)
  * text                       summary point
  QL: text / QS: text          long / short exam questions
  MCQ: q || a | *b | c || why  self-test question (* marks the answer)
  plain lines                  paragraph text
"""
import html, json, re, sys
from pathlib import Path

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

def parse(text):
    meta = {"reading": []}
    chapters = []
    ch = None
    indraft = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if indraft:
            ch["lines"].append(line)
            if line.strip() == "END":
                indraft = False
            continue
        if line.startswith("DRAFT: ") and ch is not None:
            indraft = True
            ch["lines"].append(line)
            continue
        if line.startswith("@") and ch is None or (line.startswith("@") and line.split()[0] in ("@title","@subtitle","@paper","@sem","@color","@dark","@intro","@reading","@marks1","@marks2")):
            k, _, v = line[1:].partition(" ")
            if k == "reading":
                meta["reading"].append(v.strip())
            elif k == "topics" and ch is not None:
                ch["topics"] = [t.strip() for t in v.split(";") if t.strip()]
            else:
                meta[k] = v.strip()
            continue
        if line.startswith("# "):
            num, _, title = line[2:].partition("|")
            ch = {"num": num.strip(), "title": title.strip(), "topics": [], "thesis": "",
                  "lines": [], "sum": [], "ql": [], "qs": [], "mcq": []}
            chapters.append(ch)
            continue
        if ch is None:
            continue
        if line.startswith("@topics"):
            ch["topics"] = [t.strip() for t in line[7:].split(";") if t.strip()]
        elif line.startswith(">> "):
            ch["thesis"] = line[3:].strip()
        elif line.startswith("* "):
            ch["sum"].append(line[2:].strip())
        elif line.startswith("QL: "):
            ch["ql"].append(line[4:].strip())
        elif line.startswith("QS: "):
            ch["qs"].append(line[4:].strip())
        elif line.startswith("MCQ: "):
            parts = line[5:].split("||")
            q = parts[0].strip()
            opts = [o.strip() for o in parts[1].split("|")]
            ans = next(i for i, o in enumerate(opts) if o.startswith("*"))
            opts = [o.lstrip("*").strip() for o in opts]
            import random, hashlib
            rnd = random.Random(int(hashlib.md5(q.encode()).hexdigest(), 16))
            order = list(range(len(opts)))
            if not any(o.lower().startswith(("all of", "none of", "both")) for o in opts):
                rnd.shuffle(order)
            opts = [opts[i] for i in order]
            ans = order.index(ans)
            ch["mcq"].append({"q": q, "o": opts, "a": ans, "w": parts[2].strip() if len(parts) > 2 else ""})
        else:
            ch["lines"].append(line)
    return meta, chapters

def render_draft(body):
    blocks, cur = [], []
    for ln in body:
        if ln.strip() == "":
            if cur: blocks.append(cur); cur = []
        else:
            cur.append(ln.rstrip())
    if cur: blocks.append(cur)
    def fmt(t):
        t = html.escape(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
        return re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    out = []
    merged = []
    for blk in blocks:
        nb, acc = [], None
        for ln in blk:
            if acc is not None:
                acc += " " + ln.strip()
                if acc.count("**") % 2 == 0:
                    nb.append(acc); acc = None
            elif ln.count("**") % 2 == 1:
                acc = ln.rstrip()
            else:
                nb.append(ln)
        if acc is not None: nb.append(acc)
        merged.append(nb)
    blocks = merged
    for blk in blocks:
        logical = []
        for ln in blk:
            st = ln.strip()
            indent = len(ln) - len(ln.lstrip())
            marker = st.startswith(("...", "(")) or re.match(r"^(\d+\.|[a-z]\)|\([a-z]+\))\s", st)
            prev = logical[-1] if logical else ""
            soft = bool(logical) and not marker and " ... " not in " " + st and not re.search(r"[.:;!?]$", prev) and "**" not in prev and "   " not in prev.strip() and (st[:1].islower() or re.search(r"(,| at| of| and| the| to| for| by| with| from)$", prev))
            if re.fullmatch(r"[A-Z][A-Z ()/.,-]{2,}", st):
                soft = False; marker = True
            starts_new = not soft and (not logical or indent < 2 or marker)
            if starts_new:
                logical.append(st)
            else:
                logical[-1] += " " + st
        lines = []
        for lg in logical:
            parts = [p for p in re.split(r"\s{3,}", lg) if p]
            if len(parts) >= 2:
                lines.append('<span class="dl"><span>' + fmt(parts[0]) + '</span><span>' + fmt(" ".join(parts[1:])) + '</span></span>')
            elif lg.startswith("..."):
                lines.append('<span class="dr">' + fmt(lg) + '</span>')
            else:
                lines.append(fmt(lg))
        out.append("<p>" + "".join(l if l.startswith('<span class="d') else '<span class="ln">' + l + '</span>' for l in lines) + "</p>")
    return "".join(out)

MAXIMS = []

def render_body(lines, cases, unit):
    out = []
    para, ul, ol, table = [], [], [], []
    def flush():
        nonlocal para, ul, ol, table
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if ul:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in ul) + "</ul>"); ul = []
        if ol:
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in ol) + "</ol>"); ol = []
        if table:
            head, *rows = table
            cls = "stack" if len(head) > 2 else "two"
            t = f'<div class="scroll"><table class="{cls}"><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f'<td data-l="{html.escape(head[i] if i < len(head) else "")}">{inline(c)}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
            out.append(t + "</tbody></table></div>"); table = []
    draft = None
    for line in lines:
        if draft is not None:
            if line.strip() == "END":
                title, body = draft
                out.append(f'<figure class="draft"><figcaption><span class="tag">Model draft</span>{inline(title)}</figcaption><div class="dbody">{render_draft(body)}</div></figure>')
                draft = None
            else:
                draft[1].append(line)
            continue
        if line.startswith("DRAFT: "):
            flush(); draft = (line[7:].strip(), []); continue
        s = line.strip()
        if not s:
            flush(); continue
        if s.startswith("|"):
            if para or ul or ol:
                t = table; table = []; flush(); table = t
            table.append([c.strip() for c in s.strip("|").split("|")]); continue
        elif table:
            flush()
        if s.startswith("## "):
            flush(); out.append(f"<h3>{inline(s[3:])}</h3>")
        elif s.startswith("### "):
            flush(); out.append(f"<h4>{inline(s[4:])}</h4>")
        elif s.startswith("- "):
            if para or ol: flush()
            ul.append(s[2:])
        elif re.match(r"^\d+\. ", s):
            if para or ul: flush()
            ol.append(re.sub(r"^\d+\. ", "", s))
        elif s.startswith("SEC: "):
            flush(); lab, _, txt = s[5:].partition("::")
            out.append(f'<aside class="box sec"><span class="tag">Statute</span><b>{inline(lab.strip())}</b><p>{inline(txt.strip())}</p></aside>')
        elif s.startswith("CASE: "):
            flush(); name, _, txt = s[6:].partition("::")
            name = name.strip(); cid = "c-" + slug(name)
            cases.append((name, unit, cid))
            out.append(f'<aside class="box case" id="{cid}"><span class="tag">Case</span><b class="cn">{inline(name)}</b><p>{inline(txt.strip())}</p></aside>')
        elif s.startswith("MAXIM: "):
            flush(); parts = [x.strip() for x in s[7:].split("::")]
            lat, tr, ex = (parts + ["", ""])[:3]
            mid = "m-" + slug(lat)
            if any(m[3] == mid for m in MAXIMS): mid += "-" + unit
            MAXIMS.append((lat, tr, unit, mid))
            out.append(f'<aside class="box max" id="{mid}"><span class="tag">Maxim</span><b class="mx">{inline(lat)}</b><p class="tr">{inline(tr)}</p>{"<p>" + inline(ex) + "</p>" if ex else ""}</aside>')
        elif s.startswith("NOTE: "):
            flush(); out.append(f'<aside class="box note"><span class="tag">Current law</span><p>{inline(s[6:])}</p></aside>')
        elif s.startswith("TIP: "):
            flush(); out.append(f'<aside class="box tip"><span class="tag">Exam tip</span><p>{inline(s[5:])}</p></aside>')
        else:
            if ul or ol: flush()
            para.append(s)
    flush()
    return "\n".join(out)

def parse_paper(text):
    """Practice paper file: PART: A | title | instruction | marks-line ; Q: [n] question ; answer lines."""
    parts, cur, q = [], None, None
    meta = {}
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("@") and cur is None:
            k, _, v = line[1:].partition(" "); meta[k] = v.strip(); continue
        if line.startswith("PART: "):
            bits = [b.strip() for b in line[6:].split("|")]
            cur = {"id": bits[0], "title": bits[1], "inst": bits[2], "marks": bits[3], "qs": []}
            parts.append(cur); q = None; continue
        if line.startswith("Q: ") and cur is not None:
            q = {"q": line[3:].strip(), "a": []}; cur["qs"].append(q); continue
        if q is not None:
            q["a"].append(line)
    return parts, meta

def render_paper(parts, label, title="Practice paper with model answers"):
    n = 0; out = []
    for pt in parts:
        out.append(f'<h3 class="ph"><span>Part {html.escape(pt["id"])}</span> {inline(pt["title"])}<small>{inline(pt["marks"])}</small></h3><p class="pi">{inline(pt["inst"])}</p>')
        for q in pt["qs"]:
            n += 1
            al = []; indr = False
            for l in q["a"]:
                al.append(l)
                st = l.strip()
                if st.startswith("DRAFT: "): indr = True; continue
                if indr:
                    if st == "END": indr = False
                    continue
                if st and not re.match(r"^(- |\d+\. |#|\|)", st):
                    al.append("")
            ans = render_body(al, [], "paper")
            out.append(f'<details class="pq" id="pq-{n}"><summary><span class="qn">{n}.</span><span class="qt">{inline(q["q"])}</span></summary><div class="ans"><span class="tag">Model answer</span>{ans}</div></details>')
    return f'''<article class="unit paper" id="paper">
<header><span class="un">Exam practice</span><h2>{inline(title)}</h2><p class="thesis">{inline(label)}</p></header>
<div class="pbar"><button type="button" id="pall">Show all answers</button><span>Try each question first, then open it to compare with the model answer.</span></div>
<div class="body">{"".join(out)}</div>
<footer class="uf"><a class="next" href="#cases">Go to the case index</a></footer>
</article>'''

def build(src, dst, template):
    meta, chapters = parse(Path(src).read_text(encoding="utf-8"))
    cases = []
    pf = Path(src).parent / "papers" / Path(src).name
    paper_parts, pmeta = parse_paper(pf.read_text(encoding="utf-8")) if pf.exists() else ([], {})
    chap_html, toc, shelf = [], [], []
    for i, ch in enumerate(chapters):
        uid = f"u{ch['num']}"
        body = render_body(ch["lines"], cases, uid)
        topics = ""
        if ch["topics"]:
            topics = '<details class="syl"><summary>What the syllabus lists for this unit</summary><ul>' + "".join(f"<li>{inline(t)}</li>" for t in ch["topics"]) + "</ul></details>"
        summ = ""
        if ch["sum"]:
            summ = '<section class="sum"><h3>Points to remember</h3><ul>' + "".join(f"<li>{inline(x)}</li>" for x in ch["sum"]) + "</ul></section>"
        qs = ""
        if ch["ql"] or ch["qs"]:
            qs = '<section class="qs"><h3>Exam questions</h3>'
            if ch["ql"]:
                qs += '<h4>Essay questions</h4><ol>' + "".join(f"<li>{inline(x)}</li>" for x in ch["ql"]) + "</ol>"
            if ch["qs"]:
                qs += '<h4>Short notes</h4><ul class="chips">' + "".join(f"<li>{inline(x)}</li>" for x in ch["qs"]) + "</ul>"
            qs += "</section>"
        quiz = ""
        if ch["mcq"]:
            quiz = f'<section class="quiz" data-u="{uid}"><h3>Check yourself</h3>'
            for qi, m in enumerate(ch["mcq"]):
                quiz += f'<div class="mcq" data-a="{m["a"]}"><p class="mq">{qi+1}. {inline(m["q"])}</p><div class="opts">'
                quiz += "".join(f'<button type="button" data-i="{oi}">{inline(o)}</button>' for oi, o in enumerate(m["o"]))
                quiz += f'</div><p class="why" hidden>{inline(m["w"])}</p></div>'
            quiz += "</section>"
        nxt = f'<a class="next" href="#u{chapters[i+1]["num"]}">Next: Unit {chapters[i+1]["num"]}, {inline(chapters[i+1]["title"])}</a>' if i + 1 < len(chapters) else ('<a class="next" href="#paper">Next: Exam practice with model answers</a>' if paper_parts else '<a class="next" href="#cases">Go to the case index</a>')
        chap_html.append(f'''<article class="unit" id="{uid}">
<header><span class="un">Unit {ch["num"]}</span><h2>{inline(ch["title"])}</h2>{f'<p class="thesis">{inline(ch["thesis"])}</p>' if ch["thesis"] else ''}</header>
{topics}
<div class="body">{body}</div>
{summ}{qs}{quiz}
<footer class="uf"><label class="done"><input type="checkbox" data-u="{uid}" id="done-{uid}"> Revised this unit</label>{nxt}</footer>
</article>''')
        toc.append(f'<li><a href="#{uid}" data-u="{uid}"><span>{ch["num"]}</span>{inline(ch["title"])}</a></li>')
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        shelf.append({"n": ch["num"], "t": ch["title"], "w": words})
    if MAXIMS:
        rowsm = sorted(MAXIMS, key=lambda m: re.sub(r"[^a-z]", "", m[0].lower()))
        trs = "".join(f'<tr><td><a href="#{mid}"><em>{inline(lat)}</em></a></td><td>{inline(tr)}</td><td><a href="#{u}">Unit {u[1:]}</a></td></tr>' for lat, tr, u, mid in rowsm)
        chap_html.append(f'''<section class="unit" id="maxaz">
<header><span class="un">Quick reference</span><h2>Maxims A to Z</h2><p class="thesis">{len(rowsm)} maxims, alphabetical. Each link opens the maxim with its explanation and leading case.</p></header>
<div class="scroll"><table class="stack"><thead><tr><th>Maxim</th><th>Meaning</th><th>Where</th></tr></thead><tbody>{trs}</tbody></table></div>
</section>''')
        toc.append('<li><a href="#maxaz"><span>A–Z</span>Maxims A to Z</a></li>')
    if paper_parts:
        nq = sum(len(p["qs"]) for p in paper_parts)
        label = pmeta.get("label") or meta.get("paperlabel", f"A full 70-mark paper ({nq} questions) in the pattern used for AP 3-year LL.B papers from 2024–25: Part A short notes, Part B essays, Part C problems. Set on this syllabus for practice; it is not a past VSU paper.")
        chap_html.append(render_paper(paper_parts, label, pmeta.get("title", "Practice paper with model answers")))
        toc.append(f'<li><a href="#paper" data-u="paper"><span>✎</span>{html.escape(pmeta.get("toc", "Practice paper"))}</a></li>')
    # case index
    seen = {}
    for name, unit, cid in cases:
        seen.setdefault(name, (unit, cid))
    rows = sorted(seen.items(), key=lambda kv: re.sub(r"^(the|in re|re)\s+", "", kv[0].lower()))
    case_rows = "".join(f'<tr><td><a href="#{cid}">{inline(n)}</a></td><td><a href="#{u}">Unit {u[1:]}</a></td></tr>' for n, (u, cid) in rows)
    readings = "".join(f"<li>{inline(r)}</li>" for r in meta["reading"])
    page = template
    rep = {
        "{{TITLE}}": html.escape(meta["title"]),
        "{{SUBTITLE}}": inline(meta.get("subtitle", "")),
        "{{PAPER}}": html.escape(meta["paper"]),
        "{{SEM}}": html.escape(meta["sem"]),
        "{{COLOR}}": meta["color"],
        "{{DARK}}": meta.get("dark", meta["color"]),
        "{{INTRO}}": inline(meta.get("intro", "")),
        "{{TOC}}": "".join(toc),
        "{{CHAPTERS}}": "\n".join(chap_html),
        "{{CASEROWS}}": case_rows,
        "{{NCASES}}": str(len(rows)),
        "{{NUNITS}}": str(len(chapters)),
        "{{READINGS}}": readings,
        "{{SHELF}}": json.dumps(shelf),
        "{{KEY}}": "llb-" + meta["paper"],
        "{{M1L}}": html.escape(meta.get("marks1","University exam :: 70 marks, 3 hours").split("::")[0].strip()),
        "{{M1}}": html.escape(meta.get("marks1","University exam :: 70 marks, 3 hours").split("::")[1].strip()),
        "{{M2L}}": html.escape(meta.get("marks2","Internal :: 30 marks").split("::")[0].strip()),
        "{{M2}}": html.escape(meta.get("marks2","Internal :: 30 marks").split("::")[1].strip()),
    }
    for k, v in rep.items():
        page = page.replace(k, v)
    if not rows:
        page = re.sub(r'\s*<section id="cases" class="unit">.*?</section>', '', page, flags=re.S)
        page = page.replace('<li><a href="#cases"><span>§</span>Case index</a></li>', '')
        page = page.replace('<a class="next" href="#cases">Go to the case index</a>', '<a class="next" href="#maxaz">Go to Maxims A to Z</a>' if MAXIMS else '')
    Path(dst).write_text(page, encoding="utf-8")
    tw = sum(s["w"] for s in shelf)
    print(f"{dst}: {len(chapters)} units, {len(rows)} cases, ~{tw} words, {sum(len(c['mcq']) for c in chapters)} MCQs")

if __name__ == "__main__":
    tpl = Path(__file__).with_name("template.html").read_text(encoding="utf-8")
    build(sys.argv[1], sys.argv[2], tpl)
