#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rpf'
SITENAME = 'The Real Pope Francis'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('news.va', 'https://www.news.va/'),
         )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['asciidoc_reader']

#Custom settings
CSS_FILE = 'style.css'
SUMMARY_MAX_LENGTH = None
ARTICLE_ORDER_BY = 'category'
DISPLAY_CATEGORIES_ON_MENU = 1
DISPLAY_PAGES_ON_MENU = 0
