#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import re
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/markdown-remove-section
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        section_start_regex = re.compile(kwargs.get(str('section_start_regex'), r'^# TOC$'))
        section_end_regex = re.compile(kwargs.get(str('section_end_regex'), r'^---$'))

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.remove_section(item_path, output_dir, section_start_regex, section_end_regex)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.remove_section(contained_file, output_sub_dir, section_start_regex, section_end_regex)

    @staticmethod
    def remove_section(input_file, output_dir, section_start_regex, section_end_regex):
        output_file_name = os.path.basename(input_file)
        output_file = os.path.join(output_dir, output_file_name)

        last_line_was_newline = False
        remove_this_section = False

        with codecs.open(input_file, encoding='utf-8', mode='r') as input_file_handler:
            with codecs.open(output_file, encoding='utf-8', mode='w') as output_file_handler:
                for line in input_file_handler:
                    # Check if we were inside a section that should be removed in the last line.
                    if remove_this_section:
                        # We were inside a section that should be removed. Check for the end line.
                        if section_end_regex.match(line):
                            # End line reached. Toggle flag and continue in next line.
                            remove_this_section = False
                            continue
                        else:
                            # End line NOT reached yet. Continue with the next line.
                            continue
                    else:
                        # We were NOT inside a section that should be removed in the last line. But we might be now.
                        if section_start_regex.match(line):
                            # We are now in a section that should be removed. Toggle flag and continue in next line.
                            remove_this_section = True
                            continue
                        else:
                            # This line is not within a section that should be removed. Write it to output.
                            # But avoid writing double newlines.
                            this_line_is_newline = True if len(line.strip()) == 0 else False

                            if not (last_line_was_newline and this_line_is_newline):
                                output_file_handler.write(line)

                            # Remember that a newline was written to output when writing the next line.
                            last_line_was_newline = True if this_line_is_newline else False
