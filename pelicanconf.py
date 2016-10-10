#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

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
    ('#contact', 'Call for Proposals'),
    ('#faq', 'FAQ')
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

with open('faq.yml') as f:
    FAQ = yaml.load(f)

# TODO : Some of the below text can be turned into FAQ.

"""
Thank you for submitting a proposal for the 2016 UCD MAE Department’s
Mechanical Engineering Capstone Design Course. We have reviewed your proposal
and believe that it will be a suitable project for a team of our engineering
students to tackle. This letter is intended to give you an idea of what to
expect in the relationships with the student team, the instructors, and the
department. If you are not comfortable with what is presented below it is OK
not to participate from here on forward or if you need clarification before
proceeding just let me know.


The primary educational goal of this course is for the students to demonstrate
their ability to realize a viable mechanical design from a given need.
Concurrently, you will gain a solution for your need and develop a, hopefully
lasting, relationship with our students. By participating you are supporting
the educational process, will have first contact with potential new hires, may
get a new approach to your problem/project, or possibly a valuable outcome.

The course starts on January 4th. 2016 and ends on June 9th, 2016 with spring
break at the midpoint between two ten week quarters. The students spend the
first half learning about the design process, researching, gathering, and
synthesizing information, testing ideas, and developing initial designs. The
second quarter is spent finalizing the design and potentially developing a
prototype and testing it. You, the sponsor, will play a critical role over this
period by providing the students with information, feedback, and/or mentorship.

Before the course starts I will contact you by phone or visit you in person to
discuss your project. Some of the projects may need some adjustments to
redefine the scope either to ensure that it is feasible, to best highlight our
students’ skills, or to ensure that it aligns well with the flow of the course.
Once the project is well defined, we will match projects with student teams
based on their skills and preferences.

Your student team will approach you at the beginning of the course to arrange
for an informational interview to learn more about your specific need. This can
happen through a site visit or via phone/video conferencing. Over the
course of the two quarters, the students will communicate with you regularly
for information gathering purposes and feedback on their design progress. If
you can provide technical mentorship, the students may desire more of your
time. We expect that you will be reasonably available for the students over the
period of the course. The minimum for success is likely around one to two
meetings per two weeks. The more you interact with the students, the higher
likelihood of a solution that meets and/or exceeds your expectations. We will
work to make sure that the students in turn will give their best effort to
deliver a working design and/or prototype, communicate effectively with you
about their process, and be respectful of your time.

The instructor's primary role is to guide the students through the design
process and to provide technical feedback. We will work with the students to
define the scope of the project and to set deliverables for periodic review.
This process works best when early focus is on the sponsor need, so that
students do not go into the project with a preconceived solution in mind. In
fact, they are encouraged to consider multiple possible solution strategies
before settling on one to implement. Your support of this process is
encouraged.

Our students’ goal will be to deliver your expected outcome. The instructors
will work to hold them accountable in their agreements with you but it is
important that the sponsors recognize that this is a learning process for the
students. The course provides a relatively safe environment for failure which
is an essential part of learning. With that said, all we can ultimately
guarantee to you from our student teams is a written report detailing their
design. But most teams rise to the occasion and are able to develop working
prototypes by the course’s end. Keep in mind that the students are working on
designs and prototypes, which are by definition not a consumer ready product.
It is important to also be aware that out of our 160 students in the course
each year we do occasionally have a team that underperforms.

Our course requires resources and funding to remain sustainable. The prototypes
and administration needs are funded primarily by in-kind donations from you,
the sponsors. At the minimum, if you desire a prototype, we asked that you
cover the funds for the necessary parts, materials, and any necessary external
labor. At a maximum, we ask that you make a general donation to our program. A
typical industry donation is $3000. We do not exclude non-profit and charitable
organizations that lack funds, even for the basic prototype costs. We accept
donations on a sliding scale and there are some potential internal funding
mechanisms that we can reach out to if your project fits certain criteria [2].
Please contact me if you have funding needs you cannot meet.

The issue of inventorship on potentially patentable projects sometimes arises.
The position of the university is that student inventors own their own
intellectual property, though inventorship could extend to other parties with
university affiliations that provide significant contribution. You are
encouraged to have an open dialogue with the students early on if you feel
there is commercial potential and especially if you have prior intellectual
property that impacts the project. We are not yet well equipped to host
projects that require full confidentiality. If you have this need, please let
me know as soon as possible.

Finally, we would love for you to visit the university during either the
students’ final presentations or their poster sessions and demos at the College
of Engineering Design Showcase. Past sponsors have participated on our design
review panels and for the Showcase’s judging panels.

Above all, communication is the key to a successful design experience.  If you
have any questions or concerns you are welcome to contact me at any time.
"""
