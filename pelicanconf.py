#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Varun Nayyar'
SITENAME = 'Skeptical Learning'
SITEURL = 'nayyarv.github.io'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['/Users/varun/Documents/github/pelicanplugins']
PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True

IGNORE_FILES = [".ipynb_checkpoints"]



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
         # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/varun/Documents/github/pelican-themes/pelican-striped-html5up"

