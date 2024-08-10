# -- Project information -----------------------------------------------------

project = 'Scrapo'
copyright = '2024, Yakup Cemil Kayabaş'
author = 'Yakup Cemil Kayabaş'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
