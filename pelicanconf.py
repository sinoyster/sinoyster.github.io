#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yuk Wong'
SITENAME = "Yuk's Blog"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

#DEFAULT_LANG = 'en'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE = 'fs'  # use filesystem's mtime
LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')


THEME = 'themes/niu-x2-sidebar'

from  hashlib import md5
def my_slugify(value, sep):
    m = md5(value.encode('UTF-8'))
    #m.update(value.encode("UTF-8"))
    return "toc_{}".format(m.hexdigest())
MY_SLUGIFY_FUNC = my_slugify

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.ExprStmtExtension',   ],
}

STATIC_PATHS = ['images', 'pdfs']

TEMPLATE_PAGES = {
    "archives_updatedate.html": "archives_updatedate.html",
}

# plugin config
PLUGIN_PATHS = ['./plugins/pelican-plugins', './plugins']
PLUGINS = [
    'gzip_cache',
    #'update_date',
    'extract_headings',
    #'sitemap',
    'summary',
    'render_math',
    'ipynb.markup',
    #'niux2_lazyload_helper',
    #'niux2_hermit_player',
]
UPDATEDATE_MODE = 'metadata'
