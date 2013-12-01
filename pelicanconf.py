#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Randall Degges'
SITENAME = u'Randall Degges'
SITEURL = ''

TIMEZONE = 'UTC'

IGNORE_FILES = (['.#*', 'README.md'])

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'

ARTICLE_LANG_URL = '{lang}/{slug}'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

AUTHORS_URL = 'authors'
AUTHORS_SAVE_AS = 'authors/index.html'

ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'
