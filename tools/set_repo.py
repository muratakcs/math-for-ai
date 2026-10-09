"""Replace the placeholder GitHub user/repository in all files with your own.

Usage:  python tools/set_repo.py <github-username> [<repository-name>]
Example: python tools/set_repo.py janedoe math-for-ai
Run it once after creating your repository, then commit the changes.
"""
import sys
from pathlib import Path

if len(sys.argv) not in (2, 3):
    sys.exit(__doc__)
user = sys.argv[1]
repo = sys.argv[2] if len(sys.argv) == 3 else "math-for-ai"

ROOT = Path(__file__).resolve().parent.parent
replacements = {
    "YOUR-GITHUB-USERNAME.github.io/math-for-ai": f"{user}.github.io/{repo}",
    "YOUR-GITHUB-USERNAME/math-for-ai": f"{user}/{repo}",          # github.com and Colab links
    "YOUR-GITHUB-USERNAME": user,
}
changed = 0
for path in ROOT.rglob("*"):
    if path.suffix not in {".md", ".yml", ".ipynb", ".py"} or "_build" in path.parts or path.name == "set_repo.py":
        continue
    text = path.read_text(encoding="utf-8")
    new = text
    for old, rep in replacements.items():
        new = new.replace(old, rep)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1
        print("updated", path.relative_to(ROOT))
print(f"{changed} file(s) updated for {user}/{repo}.")
