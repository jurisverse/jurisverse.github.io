# LL.B Study Books

Interactive study books for the **Vikrama Simhapuri University (VSU) 3-year LL.B syllabus (2025-26 onwards)**, one per paper across all six semesters, plus three companion guides. Law is stated as of November 2026: the BNS, BNSS and BSA (with old IPC, CrPC and Evidence Act numbers in brackets), the Labour Codes, and Supreme Court and High Court rulings up to November 2026.

Each book is a single, self-contained HTML file. Open it in any browser, on a phone or a computer. Every book has:

- units following the syllabus, with statute boxes, case boxes and current-law notes;
- a searchable case index (and an A to Z index in the maxims guide);
- points to remember, likely exam questions and self-test quizzes at the end of each unit;
- a practice paper with model answers (viva practice sets for Drafting and Moot Court);
- a revision tracker that saves progress in the browser.

**Read online: https://jurisverse.github.io/**

The site is published with GitHub Pages from the `docs/` folder of the `main` branch. The library page is [`docs/index.html`](docs/index.html).

### Semester I

| Paper | Book |
|---|---|
| 1.1 | [Contracts – I](docs/contracts-1.html) |
| 1.2 | [Constitutional Law – I](docs/constitution-1.html) |
| 1.3 | [Law of Torts and Consumer Protection](docs/torts.html) |
| 1.4 | [Law of Crimes – I](docs/crimes-1.html) |
| 1.5 | [Family Law – I](docs/family-1.html) |
### Semester II

| Paper | Book |
|---|---|
| 2.1 | [Contracts – II](docs/contracts-2.html) |
| 2.2 | [Constitutional Law – II](docs/constitution-2.html) |
| 2.3 | [Environmental Law](docs/environmental.html) |
| 2.4 | [Jurisprudence](docs/jurisprudence.html) |
| 2.5 | [Administrative Law](docs/administrative.html) |
### Semester III

| Paper | Book |
|---|---|
| 3.1 | [Property Law](docs/property.html) |
| 3.2 | [Labour Law – I](docs/labour-1.html) |
| 3.3 | [Company Law](docs/company.html) |
| 3.4 | [Public International Law](docs/pil.html) |
| 3.5 | [Interpretation of Statutes](docs/interpretation.html) |
### Semester IV

| Paper | Book |
|---|---|
| 4.1 | [Labour Law – II](docs/labour-2.html) |
| 4.2 | [Family Law – II](docs/family-2.html) |
| 4.3 | [Taxation Law](docs/taxation.html) |
| 4.4 | [Intellectual Property Rights Law](docs/ipr.html) |
| 4.5 | [Land Law including Tenure and Tenancy System](docs/land.html) |
### Semester V

| Paper | Book |
|---|---|
| 5.1 | [Civil Procedure Code and Limitation Act](docs/cpc.html) |
| 5.2 | [Law of Crimes – II: Bharatiya Nagarik Suraksha Sanhita, 2023](docs/bnss.html) |
| 5.3 | [Law of Evidence: Bharatiya Sakshya Adhiniyam, 2023](docs/bsa.html) |
| 5.4 | [Law of Banking](docs/banking.html) |
| 5.5 | [Media Law with Right to Information Act](docs/media.html) |
### Semester VI

| Paper | Book |
|---|---|
| 6.1 | [Drafting, Pleading and Conveyancing](docs/drafting.html) |
| 6.2 | [Professional Ethics and Accounting System](docs/ethics.html) |
| 6.3 | [Alternative Dispute Resolution including Mediation](docs/adr.html) |
| 6.4 | [Moot Court Exercise and Internship](docs/moot.html) |
| 6.5 | [Penology and Victimology](docs/penology.html) |
### Companion guides

| Book | What it covers |
|---|---|
| [Legal Maxims](docs/maxims.html) | The Latin (and equity) maxims an LL.B student needs, grouped by subject, with meaning, explanation and the leading case for each |
| [Legal Writing](docs/writing.html) | How to write exam answers, research and cite the law, brief a case, and write memos, opinions, papers and letters in clear legal English |
| [Bail and Bail Conditions](docs/bail.html) | A practical guide for young lawyers under the BNSS: kinds of bail, where to apply, how to argue, conditions, sureties, cancellation and special statutes |

## Repository layout

| Path | Contents |
|---|---|
| `docs/` | The built books (HTML) and the library page |
| `src/content/` | Source text of each book, in a simple plain-text format |
| `src/content/papers/` | Practice papers and exercises with model answers |
| `src/build.py`, `src/template.html` | The builder that turns a source file into a book |
| `tools/build_all.sh` | Rebuilds every book into `docs/` |
| `tools/ftest.py` | Browser test of quizzes, search and case links (needs Playwright and Chrome) |
| `tools/upd2026.py` | Script used to add the 2025-26 judgment updates |

## Rebuilding

```bash
./tools/build_all.sh                  # rebuild all books into docs/
python3 src/build.py src/content/5.2.txt docs/bnss.html   # rebuild one book
```

The source format is described at the top of `src/build.py`. In short: `# N | Unit title` starts a unit; `CASE: Name (year) :: text`, `SEC:`, `NOTE:` and `TIP:` make boxes; `MAXIM: Latin :: meaning :: explanation` makes a maxim box; `* ` lines are summary points; `QL:`/`QS:` are exam questions; `MCQ: question || a | *b | c || why` is a quiz question; `DRAFT: title` ... `END` is a model draft.

## Disclaimer

These books are study aids, not legal advice. Practice papers are set on the syllabus for practice; they are not past VSU papers. Always check the current bare act and the full judgment before relying on a point in practice.
