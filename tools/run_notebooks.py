"""Execute every notebook under notebooks/ and fail if any cell raises an error.

Usage:  python tools/run_notebooks.py            (all notebooks)
        python tools/run_notebooks.py path.ipynb (selected notebooks)
"""
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parent.parent
paths = [Path(p) for p in sys.argv[1:]] or sorted((ROOT / "notebooks").rglob("*.ipynb"))
paths = [p for p in paths if ".ipynb_checkpoints" not in p.parts]

failed = []
for path in paths:
    nb = nbformat.read(path, as_version=4)
    start = time.time()
    try:
        NotebookClient(nb, timeout=300, kernel_name="python3",
                       resources={"metadata": {"path": str(path.parent)}}).execute()
        crosses = sum(o.get("text", "").count("❌") for c in nb.cells if c.cell_type == "code"
                      for o in c.get("outputs", []) if o.get("output_type") == "stream")
        status = "OK" if crosses == 0 else f"OK, but {crosses} failing check(s) (❌)"
        if crosses:
            failed.append(path)
        print(f"{status:<10} {time.time() - start:5.1f}s  {path.relative_to(ROOT)}")
    except CellExecutionError as err:
        failed.append(path)
        print(f"FAILED           {path.relative_to(ROOT)}\n{err}")

if failed:
    sys.exit(f"\n{len(failed)} notebook(s) failed.")
print(f"\nAll {len(paths)} notebook(s) ran successfully.")
