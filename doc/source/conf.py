# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('../..'))
# sys.path.insert(0, os.path.abspath('../src'))

current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "../../src"))
sys.path.insert(0, target_dir)

print(target_dir)



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Stylometry'
copyright = '2022, Noah Krieger'
author = 'Noah Krieger'
release = '0.01'
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_rtd_theme",
                'sphinx.ext.autodoc',
                'sphinx.ext.autosummary',
                'sphinx_copybutton',
                'sphinx_toggleprompt',
                'autodocsumm',
                'sphinx.ext.mathjax',
                # 'sphinx.ext.imgmath',
                "sphinx_math_dollar"
              ]

templates_path = ['_templates']
exclude_patterns = []

autodoc_default_options = {"autosummary": True}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Generate _autosummary stub files as part of the build process
autosummary_generate = True

# Configure toggleprompt
toggleprompt_offset_right = 25  # stops toggle and copy buttons overlapping

mathjax3_config = {
  "tex": {
    "inlineMath": [['\\(', '\\)']],
    "displayMath": [["\\[", "\\]"]],

  },
    'chtml': {
        'mtextInheritFont': 'true',
    },
}