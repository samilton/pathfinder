# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pathfinder'
copyright = '2023, Elliott Management'
author = 'Sam Hamilton'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for Mermaid output ----------------------------------------------
mermaid_init_js = """
var config = {
    startOnLoad: true,
    flowchart: {
        useMaxWidth: false,
        htmlLabels: true
    },
    sequence: {
        useMaxWidth: false
    },
    gantt: {
        axisFormatter: [
            ['%I:%M', function(d) {
                return d.getHours();
            }]
        ],
        barHeight: 20,
        barGap: 4,
        topPadding: 50,
        leftPadding: 75,
        gridLineStartPadding: 35,
        gridLineEndPadding: 35,
        includeWeekend: true,
        useWidth: 1000
    }
};
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
}


html_static_path = ['_static']
