"""Build index.html: compile Tailwind (no runtime CDN), inline the CSS and the Bayt logo.

Usage: python build.py [path-to-tailwindcss-binary]
Default binary: npx tailwindcss (requires tailwindcss@3.4.17).
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
tw = sys.argv[1] if len(sys.argv) > 1 else "npx tailwindcss"

css = subprocess.run(
    f'{tw} -c tailwind.config.js -i src/input.css --minify',
    cwd=ROOT, shell=True, check=True, capture_output=True, text=True,
).stdout

svg = open(os.path.join(ROOT, "assets", "bayt-logo.svg"), encoding="utf-8").read()
svg = re.sub(r"<\?xml.*?\?>|<!--.*?-->|<title>.*?</title>|<desc>.*?</desc>|<defs></defs>", "", svg, flags=re.S)
svg = re.sub(r'\s(width|height)="[^"]*"', "", svg, count=2)
svg = svg.replace("<svg ", '<svg role="img" aria-label="Bayt.com" ', 1)
svg = re.sub(r">\s+<", "><", svg).strip()

src = open(os.path.join(ROOT, "src", "index.src.html"), encoding="utf-8").read()
out = src.replace("<!--TAILWIND-->", "<style>" + css + "</style>").replace("<!--BAYT_LOGO-->", svg)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(out)
print(f"index.html written: {len(out) // 1024} KB, css {len(css) // 1024} KB")
