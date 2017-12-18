# -*- coding: utf-8 -*-
#
# xo documentation build configuration file, created by
# sphinx-quickstart on Sun Jan 27 00:12:33 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import json
import tempfile
from textwrap import indent

import cloud_sptheme as csp

from regolith import __version__ as REGOLITH_VERSION
from regolith.fsclient import json_to_yaml
from regolith.schemas import SCHEMAS, EXEMPLARS

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode']

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'regolith'
copyright = u'2015, Anthony Scopatz'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = REGOLITH_VERSION.rsplit('.', 1)[0]

# The full version, including alpha/beta/rc tags.
release = REGOLITH_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'collections/blank.rst']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
pygments_style = 'pastie'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'redcloud'
# html_theme = 'blackcloud'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}
html_theme_options = {"roottarget": "index"}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
# html_theme_path = [csp.get_theme_dir()]
html_theme_path = ['_themes', csp.get_theme_dir()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "regolith - software group content managment system"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "regolith"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/regolith-logo.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/regolith-logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'regolithdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'regolith.tex', u'Regolith Documentation',
     u'Anthony Scopatz', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'regolith', u'regolith docs',
     [u'Anthony Scopatz'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'regolith', u'regolith documentation',
     u'Anthony Scopatz', 'regolith', 'Research group managment software.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

schema_top_docs = {
    'abstracts': 'Abstracts for a conference or workshop. This is generally public information\n\n',
    'assignments': 'Information about assignments for classes.\n\n',
    'blank': '\n',
    'blog': 'This collection represents blog posts written by the members of the research group.\n\n',
    'citations': 'This collection should contain bibtex equivalent fields.  Additionally,\nthe keys ``"entrytype"`` denotes things like ``ARTICLE``, and ``"_id"`` denotes\nthe entry identifier.  Furthermore, the ``"author"`` key should be a list of\nstrings.  See the Python project `BibtexParser <https://bibtexparser.readthedocs.org/>`_\nfor more information.\n\n',
    'courses': 'This is a collection that describes a course, when it happened, and\nwho is taking it. This is likely private.\n\n',
    'grades': 'The grade for a student on an assignment. This information should be private.\n\n',
    'grants': 'This collection represents grants that have been awarded to the group.\n\n',
    'jobs': 'This collection describes the research group jobs. This is normally public data.\n\n\n',
    'news': 'This collection describes the research group news. This is normally public data.\n\n',
    'people': 'This collection describes the members of the research group.  This is normally public\ndata.\n\n',
    'projects': 'This collection describes the research group projects. This is normally public data.\n\n',
    'proposals': 'This collection represents proposals that have been submitted by the group.\n\n',
    'students': 'This is a collection of student names and metadata. This should probably be private.\n\n'}

from pprint import pprint
import string


def format_key(schema, key, indent_str=''):
    s = ''
    line_format = ':{key}: {type}, {description}, required\n'
    line_format_o = ':{key}: {type}, {description}, optional\n'
    if not schema.get('required', False):
        lf = line_format_o
    else:
        lf = line_format
    if 'type' in schema and 'description' in schema:
        s += indent(lf.format(key=key,
                              description=schema.get('description', ''),
                              type=schema.get('type', '')), indent_str)
    elif 'type' in schema[key]:
        s += indent(lf.format(key=key,
                              description=schema[key].get('description', ''),
                              type=schema[key].get('type', '')), indent_str)
    s = s.replace(', , ', ', ')
    for inner_key in schema.get('schema', ()):
        s += format_key(schema['schema'], inner_key,
                        indent_str=indent_str + '\t')

    return s


def build_schema_doc(key):
    fn = 'collections/' + key + '.rst'
    with open(fn, 'w') as f:
        s = ''
        s += key.title() + '\n'
        s += '=' * len(key) + '\n'
        s += schema_top_docs[key]
        s += 'Schema\n------\nThe following lists key names mapped to its type and meaning for each entry.\n\n'
        schema = SCHEMAS[key]
        schema_list = list(schema.keys())
        schema_list.sort()
        for k in schema_list:
            s += format_key(schema[k], key=k)
        s += '\n\n'
        s += 'YAML Example\n------------\n\n'
        s += '.. code-block:: yaml\n\n'
        temp = tempfile.NamedTemporaryFile()
        temp2 = tempfile.NamedTemporaryFile()
        with open(temp.name, 'w') as ff:
            json.dump(EXEMPLARS[key], ff)
        jd = json.dumps(EXEMPLARS[key], sort_keys=True,
                        indent=4, separators=(',', ': '))
        json_to_yaml(temp.name, temp2.name)
        with open(temp2.name, 'r') as ff:
            s += indent(ff.read(), '\t')
        s += '\n\n'
        s += 'JSON/Mongo Example\n------------------\n\n'
        s += '.. code-block:: json\n\n'
        s += indent(jd, '\t')
        s += '\n'
        f.write(s)


for k in SCHEMAS:
    build_schema_doc(k)
