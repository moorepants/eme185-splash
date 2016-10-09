#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jason K. Moore, PhD'
SITENAME = u'MECH-CAP'
SITESUBTITLE = 'UC Davis Mechanical Engineering Capstone'
SITEURL = ''

THEME = 'theme'
THEME_STATIC_DIR = 'static'
PATH = 'content'
STATIC_PATHS = ['images', 'js', 'css', 'fonts']
TIMEZONE = 'US/Pacific'

DEFAULT_DATE_FORMAT = ('%Y')

DEFAULT_LANG = u'en'
BOOTSTRAP_FILE = 'bootstrap.css'
CSS_FILE = 'freelancer.css'
FONTS = 'fonts'

SCRIPTS = [
    'jquery-1.11.0.js',
    'bootstrap.min.js',
    'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
    'classie.js',
    'cbpAnimatedHeader.js',
    'jqBootstrapValidation.js',
    'contact_me.js',
    'freelancer.js',
    'attachment.js',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']

# Top Menu Links
NAVLINKS = (
    ('#page-top', ''),
    ('#about', 'About'),
    ('#portfolio', 'Past Projects'),
    ('#contact', 'Call for Proposals')
)

# Portfolio Name
PORTFOLIO = 'Past Projects'

# Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
    ['Name', 'text', 'name', 'Please enter your name.'],
    ['Organization', 'text', 'org', 'Please enter your company or institution.'],
    ['Email Address', 'email', 'email', 'Please enter your email address.'],
    ['Phone Number', 'tel', 'phone', 'Please enter your phone number.'],
    ['Proposal Title', 'text', 'title', 'Please enter your proposal title.'],
    ['Proposal Text (an additional single file attachment is also supported below)', 'textarea', 'message', 'Please enter a proposal.']
)
