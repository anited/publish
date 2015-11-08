#!/usr/bin/env python3
# coding: utf8
#
# apub - Python package with cli to turn markdown files into ebooks
# Copyright (C) 2015  Christopher Knörndel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from abc import ABCMeta, abstractmethod


class Output(metaclass=ABCMeta):
    def __init__(self):
        self.name = None
        self.path = None
        self.css = None
        self.force_publish = False

    @abstractmethod
    def make(self, project):
        pass

    @classmethod
    def from_dict(cls, dict_):
        output_type = dict_['type']

        if output_type == 'html':
            from .html import HtmlOutput
            output = HtmlOutput.from_dict(dict_)
        elif output_type == 'json':
            from .json import JsonOutput
            output = JsonOutput.from_dict(dict_)
        elif output_type == 'ebook-convert':
            from .ebookconvert import EbookConvertOutput
            output = EbookConvertOutput.from_dict(dict_)
        else:
            raise NotImplementedError(
                'Unrecognized output type: {0}'.format(output_type))

        output.name = dict_['name']
        output.path = dict_['path']
        output.css = dict_['css']
        output.force_publish = dict_['force_publish']

        return output

    @staticmethod
    def filter_chapters_by_publish(chapters, publish=True):
        for chapter in chapters:
            if chapter.publish == publish:
                yield chapter
