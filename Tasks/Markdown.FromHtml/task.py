#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import html2text
import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/markdown-from-html
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.convert_to_html(item_path, output_dir)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.convert_to_html(contained_file, output_sub_dir)

    @staticmethod
    def convert_to_html(input_file, output_dir):
        output_file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, output_file_name + '.md')

        with codecs.open(input_file, encoding='utf-8', mode='r') as input_file_handler:
            html_lines = input_file_handler.readlines()
            markdown_lines = []
            for line in html_lines:
                markdown_lines.append(html2text.html2text(line))

        for n, line in enumerate(markdown_lines):
            markdown_lines[n] = line.replace('\n', ' ').replace('\xa0', ' ')

        with codecs.open(output_file, encoding='utf-8', mode='w') as output_file_handler:
            for line in markdown_lines:
                output_file_handler.write(line + '\n')
