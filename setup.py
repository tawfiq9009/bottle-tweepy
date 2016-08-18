#!/usr/bin/env python

import sys
import os
from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = 'bottle-tweepy',
    version = '0.1',
    url = 'http://github.com/tawfiq9009/bottle-tweepy/',
    description = 'Tweepy integration for Bottle.',
    author = 'Tawfiq Hamed',
    author_email = 'tawfiq9009@gmail.com',
    license = 'MIT',
    platforms = 'any',
    py_modules = [
        'bottle_tweepy'
    ],
    requires = [
        'bottle (>=0.9)',
        'tweepy'
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass = {'build_py': build_py}
)