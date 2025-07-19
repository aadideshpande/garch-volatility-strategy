# 📈 GARCH Volatility Strategy

This project implements a volatility-aware trading strategy using a **GARCH(1,1)** model to detect market regimes and adjust exposure based on predicted risk.

It also includes:
- 📓 A fully automated Jupyter notebook pipeline
- 🔁 Automation using `doit`
- 📘 Documentation via Sphinx and `nbsphinx`
- 🌐 Optional GitHub Pages deployment

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Run the Notebook (Manually or via `doit`)

**Manual (recommended for first-time debugging):**

```bash
jupyter notebook notebooks/volatility_strategy.ipynb
```

**Automated:**

```bash
doit run_notebook
```

This runs and saves an executed copy to `notebooks/volatility_strategy_executed.ipynb`.

---

### 3. Build the Documentation

```bash
doit build_docs
```

This compiles your docs and notebook into HTML output at `docs/_build/index.html`.

---

### 4. View the Docs

```bash
open docs/_build/index.html
```

Or deploy them to GitHub Pages for public sharing.

---

## 📊 Strategy Overview

* Fits a **GARCH(1,1)** model to SPY log returns
* Detects **low vs high volatility regimes**
* Applies a rule-based strategy:

  * Stay invested when volatility is low
  * Exit or reduce exposure when volatility is high
* Compares performance vs buy-and-hold:

  * Sharpe Ratio
  * CAGR
  * Max Drawdown

---

## 🔧 Common Issues

| Problem                         | Fix                                                   |
| ------------------------------- | ----------------------------------------------------- |
| Notebook crashes via `doit`     | Use cached CSV instead of live data                   |
| `ModuleNotFoundError: nbsphinx` | Run `pip install nbsphinx`                            |
| Theme error in Sphinx           | Run `pip install sphinx_rtd_theme`                    |
| Notebook doesn’t show in docs   | Place inside `docs/notebooks/` and add to `index.rst` |

---

## 📚 References

* [ARCH Documentation](https://arch.readthedocs.io/)
* [nbsphinx](https://nbsphinx.readthedocs.io/)
* [Sphinx](https://www.sphinx-doc.org/)

---