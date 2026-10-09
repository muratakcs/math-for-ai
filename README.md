# Mathematics for AI: interactive lecture notebooks

Code-first lecture notebooks for the M.Sc. course *Mathematics for AI*, following
Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* (CUP 2020, [mml-book.com](https://mml-book.com)).

* **Website:** https://muratakcs.github.io/math-for-ai (built automatically from this repository)
* Every notebook can be opened in **Google Colab** or run directly **in the browser** (JupyterLite, no account needed).

## Repository layout

```
.
├── notebooks/                  one notebook per book section, grouped by chapter
│   └── ch02/2.3-solving-linear-systems.ipynb
├── templates/
│   └── notebook-template.ipynb the structure every new notebook starts from
├── tools/
│   ├── set_repo.py             one-time: insert your GitHub user/repo name everywhere
│   ├── new_notebook.py         create a notebook from the template + add it to _toc.yml
│   └── run_notebooks.py        execute all notebooks and report errors / failing checks
├── _config.yml, _toc.yml       website configuration (Jupyter Book)
├── intro.md                    landing page of the website
├── requirements.txt            packages for running the notebooks
├── requirements-build.txt      packages for building the website
└── .github/workflows/deploy.yml  build + publish on every push to main
```

## One-time setup

1. Create a new **public** GitHub repository, e.g. `math-for-ai`, and push these files to its `main` branch.
2. Insert your username and repository name in all links, then commit:
   ```bash
   python tools/set_repo.py <your-github-username> <repository-name>
   git commit -am "Set repository name" && git push
   ```
3. On GitHub, open **Settings → Pages** and set **Source** to **GitHub Actions**.
4. Open the **Actions** tab. The workflow *Build and deploy website* runs on every push
   (about 3 to 5 minutes). When it is green, the site is live at
   `https://<user>.github.io/<repository-name>/`.

If your repository is called `<user>.github.io` itself, the site lives at the root instead
of under `/<repository-name>`. In that case adjust the JupyterLite links in the notebooks
accordingly.

## Adding a lecture notebook

```bash
python tools/new_notebook.py 3.8 "Orthogonal Projections" "Chapter 3: Analytic Geometry"
```

This creates `notebooks/ch03/3.8-orthogonal-projections.ipynb` (with Colab/JupyterLite
badges, setup cell and display helpers already in place) and adds it to `_toc.yml`.
Then fill it in following the template's structure, check it, and push:

```bash
python tools/run_notebooks.py notebooks/ch03/3.8-orthogonal-projections.ipynb
git add . && git commit -m "Add 3.8" && git push
```

### Conventions for every notebook

1. Header with badges and learning goals, numbered like the book's sections.
2. Setup cell (also installs packages when running in JupyterLite), then the display
   helpers (hidden on the website).
3. Per concept: **intuition → definition in LaTeX → from-scratch implementation →
   visualization / step-through → comparison with numpy or sympy → 🤔 Predict prompt**.
4. Exact arithmetic with `sympy` where students compare with pen-and-paper work;
   `numpy` floating point where numerical behaviour matters.
5. ✍️ Exercises: a stub returning `None`, a test cell printing ✅ / ❌ / ⏳, and a solution in
   a collapsed `<details>` block. Tests never raise errors, so the website build doesn't
   fail on unfinished exercises.
6. **Commit notebooks without outputs**, so that students don't see the answers to Predict
   prompts before running the cells. (The website executes them itself.)
   Optional: `pip install nbstripout && nbstripout --install` does this automatically.

## Local preview

```bash
pip install -r requirements-build.txt
python tools/run_notebooks.py                     # check that everything runs
jupyter-book build .                              # website -> _build/html/index.html
jupyter lite build --contents notebooks --output-dir _build/html/lite
python -m http.server -d _build/html 8000         # open http://localhost:8000
```

(JupyterLite must be served over HTTP; opening the files directly does not work.)

## Good to know

* **Colab:** changes are lost unless students use *File → Save a copy in Drive*.
* **JupyterLite:** the first start takes 10 to 30 seconds (it downloads Python into the
  browser). Work is saved in the browser's storage only; students should download notebooks
  they want to keep. Only pure-Python packages and packages shipped with Pyodide are
  available; numpy, sympy, matplotlib and ipywidgets all work.
* **Website:** interactive widgets such as the step-through slider need a running kernel.
  On the static site they show their initial state only; every notebook therefore also
  prints the full step sequence.

Book content © Deisenroth, Faisal & Ong. Notebooks: add the licence of your choice
(e.g. CC BY 4.0 for text, MIT for code).
