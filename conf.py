# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'HERMES project'
copyright = '2022, HERMES project'
author = 'Oliver Bertuch, Stephan Druskat, Guido Juckeland, Jeffrey Kelling, Oliver Knodel, Michael Meinel, Tobias Schlauch, Sophie Kernchen'

# The full version, including alpha/beta/rc tags
release = '2022-07-01'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx-favicon',
    'sphinxcontrib.contentui',
    'sphinxcontrib.images',
    'sphinxcontrib.icon',
    'sphinxemoji.sphinxemoji',
    "sphinxext.opengraph",
    'myst_parser'
]

language = 'en'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', '.venv', 'README.md']

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True

# MyST parser options
myst_enable_extensions = [
    'tasklist',
    'deflist',
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/img/hermes-visual-blue.svg'
html_title = 'The HERMES Project'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "**": ["navbar-logo.html", "sbt-sidebar-nav.html", "funding.html"]
}

# Enable and customize the permanent headerlinks with a nice icon (chain symbol from FontAwesome)
html_permalinks = True
html_permalinks_icon = "<i class=\"fas fa-link\"></i>"

html_theme_options = {
    "home_page_in_toc": True,
    "repository_url": "https://github.com/hermes-hmc/project",
    "use_repository_button": True,
    "navigation_with_keys": False,
}

html_css_files = [
    'custom.css',
]

html_context = {
    "default_mode": "light",
}

# -- Options for OpenGraph Tags ----------------------------------------------

ogp_site_url = "https://project.software-metadata.pub/"
ogp_image = "https://project.software-metadata.pub/_static/img/opengraph.png"
ogp_image_alt = "The HERMES key visual on a green background with pipelines and the acronym written out as Helmholtz Rich Metadata Software Publications"
ogp_description_length = 200
ogp_type = "website"
