# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.abspath('../process'))


# -- Project information -----------------------------------------------------

project = 'Bangkok Liveability (preview documentation)'
copyright = '2019, Carl Higgs, Amanda Alderton, Korn Nitviminol, Hannah Badland'
author = 'Carl Higgs, Amanda Alderton, Korn Nitviminol and Hannah Badland'

# The full version, including alpha/beta/rc tags
release = '1.0'

# The master toctree document.
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxmark', 'sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"
pygments_style = 'sphinx'

html_theme_path = ["_themes", ]
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Custom changes --------------------------------------------------------
html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'logo_only': False,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
    #'style_nav_header_background':'#2ca25f'
}

# To better support Thai when producing PDF
latex_engine = 'xelatex'
latex_use_xindy = True

# Enable a draft watermark
sphinxmark_enable = True
sphinxmark_div = 'default'
sphinxmark_image = 'text'
sphinxmark_text = 'Pre-Release'
sphinxmark_text_size = 80

# -- Options for sphinxmark -----------------------------------------------
# sphinxmark_div = 'docs-body'
# sphinxmark_border = 'left'
# sphinxmark_repeat = False
# sphinxmark_fixed = True
# sphinxmark_image = 'text'
# sphinxmark_text = 'Mitaka'
# sphinxmark_text_color = (255, 0, 0)
# sphinxmark_text_size = 100
# sphinxmark_text_width = 1000
# sphinxmark_text_opacity = 50
# sphinxmark_text_spacing = 600
# sphinxmark_text_rotation = 90