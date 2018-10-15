#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# theme stuff
import sys
from datetime import datetime
sys.path.append('.')
import inflect

def ordinal(self):
    o = inflect.engine()
    return o.ordinal(self)  # 1 -> '1st'

JINJA_FILTERS = { 'ordinal': ordinal }
COPYRIGHT_YEAR = datetime.now().strftime('%Y')

# theme stuff

AUTHOR = 'Varun Nayyar'
SITENAME = 'Skeptical Learning'
SITEDESCRIPTION = 'ML without the rose tinted lenses'
DEFAULT_DATE_FORMAT = "%B %-d, %Y"

SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']


TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# this is to make jupyter notebooks an accessible category
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['/Users/varun/Documents/github/pelicanplugins']
PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True
IPYNB_GENERATE_SUMMARY = True

# if you write the ipynb directly in content
IGNORE_FILES = [".ipynb_checkpoints"]



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Top Nav menu
MENUITEMS = (('About', '/about'),
         ('Archives', '/archives'),
         ('Tags','/tags'),
         ('Categories','/categories'))

# Social widget
SOCIAL = (('github', 'https://github.com/nayyarv/'),
           ('email', 'mailto:nayyarv@gmail.com'))

STATIC_PATHS = [
    'pages',
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
}



DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# THEME = "simple"
THEME = "/Users/varun/Documents/github/pelican-html5up-halcyonic"

# themestuff
PLUGIN_PATHS.append('/Users/varun/Documents/github/pelican-plugins')
PLUGINS.append('neighbors')

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

