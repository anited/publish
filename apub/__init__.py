#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# apub - Python package with cli to turn markdown files into ebooks
# Copyright (c) 2014 Christopher Knörndel
#
# Distributed under the MIT License
# (license terms are at http://opensource.org/licenses/MIT).

from pkg_resources import resource_string

__author__ = 'Christopher Knörndel'
__email__ = 'cknoerndel@anited.de'
__version__ = resource_string(__name__, 'VERSION').decode('utf-8').strip()

# Expose the 'public' API on the top level package
from apub.book import Book, Chapter  # NOQA
from apub.substitution import SimpleSubstitution  # NOQA
from apub.output import HtmlOutput, EbookConvertOutput  # NOQA

__all__ = ['Book',
           'Chapter',
           'SimpleSubstitution',
           'HtmlOutput',
           'EbookConvertOutput']
