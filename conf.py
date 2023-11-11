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

latex_preamble = r'''
% 透かしの設定
\DraftwatermarkOptions{angle={0}}
\DraftwatermarkOptions{scale={0.15}}
\DraftwatermarkOptions{hpos={0.90\paperwidth}}
\DraftwatermarkOptions{vpos={0.20\paperwidth}}
\DraftwatermarkOptions{color={[rgb]{1, 0, 0}}}
\DraftwatermarkOptions{text={%
    \includegraphics{./../../images/maruhi_mark.png} \\ サンプル
}}
'''

latex_extrapackages = r'''
\usepackage{draftwatermark}
'''

latex_elements = {
    'papersize': 'a4paper',
    'preamble': latex_preamble,
    'extrapackages': latex_extrapackages,
}
