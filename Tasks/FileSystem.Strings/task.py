#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-copy-to-directory
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        other_args = kwargs.get(str('other_args'), '')

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.extract_strings(item_path, output_dir, other_args)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.extract_strings(contained_file, output_dir, other_args)

    @staticmethod
    def extract_strings(input_file, output_dir, other_args):
        input_file_name, input_extension = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, input_file_name + '.txt')

        command = '/usr/bin/strings '
        if len(other_args) > 0:
            command += other_args + ' '
        command += '"%s"' % input_file

        print('Calling: %s' % command)

        with open(output_file, 'w') as file_handler:
            exit_code = subprocess.call(command, shell=True, stdout=file_handler)

        if exit_code > 0:
            sys.exit(exit_code)
