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

latex_passoptionstopackages = rf'''
\makeatletter
\PassOptionsToPackage{{
    pdftitle={{{project}}},
    pdfauthor={{{author}}}
}}{{hyperref}}
\makeatother
'''

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

% ヘッダとフッタを設定
% FIXED ME: chapter の最初のページが変更できない。
\renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}}

\fancypagestyle{normal}{
    \fancyhf{}
    \fancyhead[LE]{\rightmark}
    \fancyhead[RO]{\rightmark}
    \fancyfoot[C]{\thepage}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% 表目次と図目次を追加
\makeatletter
\renewcommand{\sphinxtableofcontents}{
    \pagenumbering{roman}
    \begingroup
        \parskip
        \z@skip
        \sphinxtableofcontentshook
        \tableofcontents
        \listoffigures
        \listoftables
    \endgroup
    \if@openright
        \cleardoublepage
    \else
        \clearpage
    \fi
    \pagenumbering{arabic}
}
\makeatother
'''

latex_maketitle = r'''
\makeatletter
\begin{titlepage}
    \ThisULCornerWallPaper{0.25}{./../../images/mark_network_status_benkyouchu.png}
    \vspace*{\fill}
    \begin{center}
        \py@HeaderFamily
        {\Huge \@title \par}
        {\itshape\LARGE \py@release\releaseinfo \par}
    \end{center}
    \vspace*{\fill}
    \begin{flushright}
        {\LARGE \@date \par \@author}
    \end{flushright}
    \vspace*{\baselineskip}
\end{titlepage}
\makeatother
'''

latex_extrapackages = r'''
\usepackage{draftwatermark}
\usepackage{wallpaper}
'''

latex_elements = {
    'papersize': 'a4paper',
    'passoptionstopackages': latex_passoptionstopackages,
    'preamble': latex_preamble,
    'maketitle': latex_maketitle,
    'extrapackages': latex_extrapackages,
    'extraclassoptions': 'openany',
}
