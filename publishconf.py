#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.rdegges.com'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True


### THEME CONFIGURATION (pelican-rdegges)
SITE_URL = SITEURL
NAVIGATION_LINKS = (
    ('Home', SITE_URL),
    ('Archive', ARCHIVES_URL),
    ('Twitter', 'https://twitter.com/rdegges'),
    ('Code', 'https://github.com/rdegges'),
    ('Talks', 'https://speakerdeck.com/rdegges'),
    ('Email', 'mailto:r@rdegges.com'),
)

