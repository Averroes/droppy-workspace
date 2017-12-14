#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/text-remove-multi-newlines
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.remove_multi_newlines(input_path, output_dir)

            elif os.path.isdir(input_path):
                output_sub_dir = os.path.join(output_dir, os.path.basename(input_path))
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(input_path)
                for contained_file in contained_files:
                    self.remove_multi_newlines(contained_file, output_sub_dir)

    @staticmethod
    def remove_multi_newlines(input_file, output_dir):
        output_file_name = os.path.basename(input_file)
        output_file = os.path.join(output_dir, output_file_name)

        last_line = ''

        with codecs.open(input_file, encoding='utf-8', mode='r') as input_file_handler:
            with codecs.open(output_file, encoding='utf-8', mode='w') as output_file_handler:
                for n, line in enumerate(input_file_handler):
                    # If the last line was empty ...
                    if len(last_line.strip()) == 0:
                        # ... and this line is empty ...
                        if len(line.strip()) == 0:
                            # ... don't write it to the output file.
                            continue

                    # Otherwise write it to the output file.
                    output_file_handler.write(line)

                    # And remember this line's content when processing the next line.
                    last_line = line
