# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SiteXML'
copyright = '2025, ORFEUS'
author = 'Kyriaki Konstantinidou (kiriaki@itsak.gr)'

version = '1.3'

# Documentation version, schema + date
# ALSO UPDATE the release documentation version in overview.rst
doc_version = version + ' (2025-11-25)'

# Allow |doc_version| to be used in RST
rst_epilog = '.. |doc_version| replace:: %s' % doc_version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 0,
    'sticky_navigation': False,
}
html_logo='_static/FDSN-logo.png'
html_favicon = '_static/favicon.ico'
html_title = 'ORFEUS SiteXML'
html_show_sphinx = False
html_search_language = 'en'

navigation_depth = -2

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
  'css/custom.css',
  'css/theme_overrides.css',
]

html_js_files = [
  'js/sidebar_context.js'
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
