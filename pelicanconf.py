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
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'


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

TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
TRANSLATION_FEED_RSS = 'feeds/all-%s.rss.xml'


### THEME CONFIGURATION (pelican-rdegges)
THEME = 'theme'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'style.css'

# Specifies the author of this site (will show in the meta author tag on all
# pages).
SITE_AUTHOR = 'Randall Degges'

# The default meta description tag displayed on all page (can be overridden on
# a per-article basis).
SITE_DESCRIPTION = 'The personal website of Randall Degges: programmer, speaker, author and entrepreneur.'

# The title of this site.
SITE_TITLE = 'Randall Degges'

# The subtitle of this site.
SITE_SUBTITLE = 'Random Thoughts of a Happy Programmer'

# The fully qualified site URL (without a trailing slash).  For instance:
# http://www.rdegges.com
# If you're running this site locally (for testing), set this to the empty
# string ''.
SITE_URL = ''

# This site's Google Analytics ID.  If specified, Google Analytics will be
# automatically added to each page of the site.
GOOGLE_ANALYTICS_ID = 'UA-11364428-13'

# The default language of this site.
LANGUAGE_CODE = DEFAULT_LANG

# A list of navigation links that will show in the site's main navbar.
NAVIGATION_LINKS = (
    ('Twitter', 'https://twitter.com/rdegges'),
    ('Code', 'https://github.com/rdegges'),
    ('Talks', 'https://speakerdeck.com/rdegges'),
    ('Email', 'mailto:r@rdegges.com'),
)
