#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('docs/history.rst').read().replace('.. :changelog:', '')

requirements = [
    'markdown>=2.6',
    'validators>=0.11'
]

test_requirements = [
    'nose'
]

setup(
    name='apub',
    version='1.0.0-alpha.0',
    description='Python package with command line interface to turn markdown '
                'files into ebooks.',
    long_description=readme + '\n\n' + history,
    author='Christopher Knörndel',
    author_email='cknoerndel@anited.de',
    url='https://github.com/vomaufgang/apub/',
    packages=[
        'apub',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='apub',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
