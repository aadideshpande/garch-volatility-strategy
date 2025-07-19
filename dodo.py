from doit import create_after
from pathlib import Path


def task_fetch_data():
    return {
        'actions': [
            'PYTHONPATH=src python -m volatility_model.loader || echo "Skipping save — no data."'
        ],
        'targets': ['data/spy_returns.csv'],
        'clean': True,
    }


def task_run_notebook():
    return {
        'file_dep': ['notebooks/volatility_strategy.ipynb'],
        'targets': ['notebooks/volatility_strategy_executed.ipynb'],
        'actions': [
            'jupyter nbconvert --to notebook --execute '
            '--ExecutePreprocessor.timeout=300 '
            '--ExecutePreprocessor.kernel_name=python3 '
            '--output volatility_strategy_executed.ipynb '
            '--output-dir notebooks '
            'notebooks/volatility_strategy.ipynb'
        ],
        'clean': True,
        'verbosity': 2
    }




def task_build_docs():
    """Generate Sphinx HTML docs"""
    return {
        'actions': ['sphinx-build -b html docs docs/_build'],
        'file_dep': ['docs/index.rst', 'docs/conf.py'] + list(map(str, Path("src/volatility_model").rglob("*.py"))),
        'targets': ['docs/_build/index.html'],
        'clean': True,
    }
