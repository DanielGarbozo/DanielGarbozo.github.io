#!/usr/bin/env python
"""Render cv.html to cv.pdf (A4, one page) with headless Chromium via Playwright.

Serves the repository on a throwaway local port, waits for web fonts, prints with the
page's own @page rules, then refuses to write a PDF whose content overflows one page.

    pip install playwright && playwright install chromium
    python cv/make_cv_pdf.py

Alternative without Python (no overflow check):
    chrome --headless --no-pdf-header-footer --virtual-time-budget=20000 \
           --print-to-pdf=cv.pdf http://localhost:8000/cv.html
"""
import functools
import http.server
import pathlib
import sys
import threading

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main(executable: str | None = None) -> None:
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_address[1]}/cv.html"
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=executable) if executable else p.chromium.launch()
            page = browser.new_page()
            page.goto(url, wait_until="networkidle")
            page.emulate_media(media="print")
            page.evaluate("document.fonts.ready")
            overflow = page.evaluate(
                "(() => { const s = document.querySelector('.sheet');"
                " const last = [...s.querySelectorAll('section')].pop();"
                " const pad = parseFloat(getComputedStyle(s).paddingBottom);"
                " return last.getBoundingClientRect().bottom - s.getBoundingClientRect().top + pad - s.clientHeight; })()"
            )
            if overflow > 0:
                sys.exit(f"cv.html overflows one A4 page by {overflow:.0f}px; shorten it first")
            page.pdf(path=str(ROOT / "cv.pdf"), prefer_css_page_size=True, print_background=True)
            browser.close()
    finally:
        server.shutdown()
    print("wrote", ROOT / "cv.pdf")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
