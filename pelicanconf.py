#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Randall Degges'
SITENAME = u'Randall Degges'
SITEURL = ''

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (
    ('Code', 'http://github.com/rdegges'),
    ('Talks', 'http://speakerdeck.com/u/rdegges'),
)

# Social widget
SOCIAL = (
    ('@rdegges', 'https://twitter.com/rdegges'),
)

DEFAULT_PAGINATION = 3

THEME = 'tuxlite_tbs'


ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}/index.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

INDEX_URL = ''
INDEX_SAVE_AS = 'index.html'

TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags/index.html'

CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'

ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'

FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
