"""Create a new lecture notebook from the template and add it to the table of contents.

Usage:  python tools/new_notebook.py <section> "<title>" [<part caption>]
Example: python tools/new_notebook.py 3.8 "Orthogonal Projections" "Chapter 3: Analytic Geometry"

This creates notebooks/ch03/3.8-orthogonal-projections.ipynb and registers it in _toc.yml.
"""
import re
import sys
from pathlib import Path

if len(sys.argv) not in (3, 4):
    sys.exit(__doc__)
section, title = sys.argv[1], sys.argv[2]
chapter = int(section.split(".")[0])
caption = sys.argv[3] if len(sys.argv) == 4 else f"Chapter {chapter}"

ROOT = Path(__file__).resolve().parent.parent
slug = f"{section}-" + re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
rel = f"ch{chapter:02d}/{slug}.ipynb"
target = ROOT / "notebooks" / rel
if target.exists():
    sys.exit(f"{target} already exists.")

text = (ROOT / "templates" / "notebook-template.ipynb").read_text(encoding="utf-8")
text = (text.replace("@TITLE@", f"{section} {title}")
            .replace("@SECTION@", section)
            .replace("@PATH@", rel))
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(text, encoding="utf-8")
print("created", target.relative_to(ROOT))

# Register in _toc.yml (adds a new part for the chapter if needed).
toc_path = ROOT / "_toc.yml"
toc = toc_path.read_text(encoding="utf-8")
entry = f"      - file: notebooks/{rel[:-len('.ipynb')]}\n"
header = f'  - caption: "{caption}"\n    chapters:\n'
if header in toc:
    # insert after the last entry of this part
    start = toc.index(header) + len(header)
    nxt = toc.find("  - caption:", start)
    pos = len(toc) if nxt == -1 else nxt
    toc = toc[:pos].rstrip("\n") + "\n" + entry + toc[pos:]
else:
    toc = toc.rstrip("\n") + "\n" + header + entry
toc_path.write_text(toc, encoding="utf-8")
print("added to _toc.yml")
