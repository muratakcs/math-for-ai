# Mathematics for AI

Interactive lecture notebooks for the M.Sc. course *Mathematics for AI*, following
M. P. Deisenroth, A. A. Faisal and C. S. Ong, **Mathematics for Machine Learning**
(Cambridge University Press, 2020). The book is freely available at
[mml-book.com](https://mml-book.com).

## How to use these notebooks

Every page of this site is a Jupyter notebook. You can **read** it here, with all
outputs already computed, or **run and modify** it in one of two ways:

| | How | Good for |
|---|---|---|
| **Google Colab** | Click *Open in Colab* at the top of a notebook, or the 🚀 icon at the top of the page. | Reliable, fast, saves to your Google Drive (use *File → Save a copy in Drive*). |
| **In your browser (JupyterLite)** | Click *Run in browser* at the top of a notebook. | No account and no installation. Everything runs locally in your browser; your changes stay in that browser only. |

To run the notebooks on your own computer:

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/math-for-ai.git
cd math-for-ai
pip install -r requirements.txt
jupyter lab
```

## How each notebook works

* 🤔 **Predict**: stop and write down your expectation *before* running the next cell.
* ✍️ **Exercises** come with a test cell that prints ✅ or ❌, and a hidden solution.
* Everything is computed twice where it matters: **exactly** (with `sympy`, matching
  pen-and-paper calculations) and in **floating point** (with `numpy`, as in real ML code).

## Notebooks

```{tableofcontents}
```
