from doit import create_after
from pathlib import Path


def task_run_notebook():
    """Run Jupyter notebook and output executed version"""
    return {
        'file_dep': ['notebooks/volatility_strategy.ipynb'],
        'targets': ['notebooks/volatility_strategy_executed.ipynb'],
        'actions': ['jupyter nbconvert --to notebook --execute notebooks/volatility_strategy.ipynb --output notebooks/volatility_strategy_executed.ipynb']
    }


def task_build_docs():
    """Generate Sphinx HTML docs"""
    return {
        'actions': ['sphinx-build -b html docs docs/_build'],
        'file_dep': ['docs/index.rst', 'docs/conf.py'] + list(map(str, Path("src/volatility_model").rglob("*.py"))),
        'targets': ['docs/_build/index.html'],
        'clean': True,
    }
