import asyncio, os, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"))
        for f in sys.argv[1:]:
            pg = await b.new_page(viewport={"width":1280,"height":900})
            errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto("file://" + os.path.abspath(f"docs/{f}.html")); await pg.wait_for_timeout(500)
            m = pg.locator(".mcq").first
            await m.locator("button").nth(0).click()
            right = await m.locator("button.right").count(); why = await m.locator(".why").is_visible()
            await pg.locator(".done input").first.check()
            prog = await pg.locator("#prog").inner_text()
            await pg.fill("#find","consent")
            hits = await pg.locator("#hits a").count()
            links = await pg.evaluate("[...document.querySelectorAll('#cases td a[href^=\"#c-\"]')].filter(a=>!document.getElementById(a.getAttribute('href').slice(1))).length")
            print(f, "errs",errs,"right",right,"why",why,"prog",prog.split('\n')[0],"hits",hits,"broken case links",links)
        await b.close()
asyncio.run(main())
