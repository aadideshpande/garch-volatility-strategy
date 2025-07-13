import os
import sys


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'nbsphinx',
    'myst_parser',
]

html_theme = 'sphinx_rtd_theme'
sys.path.insert(0, os.path.abspath('../src'))
