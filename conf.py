# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sample Project'
copyright = '2023, 9506hqwy'
author = '9506hqwy'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
]

exclude_patterns = [
    '_build',
    '_latex',
    '_script',
]

language = 'ja'

# 図表番号を連番で付ける。
numfig = True
numfig_secnum_depth = 0

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_style = 'css/styles.css'

# -- Options for PDF output --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_passoptionstopackages = open('_latex/pass_options_to_packages.tex') \
    .read() \
    .format(project=project, author=author)
latex_preamble = open('_latex/preamble.tex').read()
latex_maketitle = open('_latex/maketitle.tex').read()
latex_extrapackages = open('_latex/extra_packages.tex').read()

latex_elements = {
    'papersize': 'a4paper',
    'passoptionstopackages': latex_passoptionstopackages,
    'preamble': latex_preamble,
    'maketitle': latex_maketitle,
    'extrapackages': latex_extrapackages,
    'extraclassoptions': 'openany',
}
