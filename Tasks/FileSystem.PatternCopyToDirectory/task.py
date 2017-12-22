#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import re
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import copy_file, copy_tree, home_dir_to_absolute_path
from task_tools import pass_input_to_output


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-pattern-copy-to-directory
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        patterns = kwargs.get(str('patterns'), [])
        directories = kwargs.get(str('directories'), [])
        ignore_case = kwargs.get(str('ignore_case'), True)
        overwrite = kwargs.get(str('overwrite_existing'), False)
        create = kwargs.get(str('create_directory'), False)

        # Check required arguments.
        if len(patterns) == 0:
            sys.exit('No patterns passed')
        elif len(directories) == 0:
            sys.exit('No directories passed')
        elif len(patterns) != len(directories):
            sys.exit('Different number of patterns and directories passed')

        # Process files and directories.
        compiled_patterns = self.compile_patterns(patterns, ignore_case)
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)
            self.match_and_copy(item_path, compiled_patterns, directories, overwrite, create)

        # Up to this point our Task has no output. Which means the next Task has no input to work with.
        # So we're re-using the previous Task's output, by passing it down.
        pass_input_to_output(input_dir, output_dir)

    @staticmethod
    def compile_patterns(patterns, ignore_case):
        re_flags = [re.UNICODE]
        if ignore_case:
            re_flags.append(re.IGNORECASE)

        bit_flags = 0
        for re_flag in re_flags:
            bit_flags = bit_flags | re_flag

        compiled_patterns = []
        for pattern in patterns:
            compiled_patterns.append(re.compile(pattern, flags=bit_flags))

        return compiled_patterns

    @classmethod
    def match_and_copy(cls, input_path, compiled_patterns, directories, overwrite, create):
        for n, compiled_pattern in enumerate(compiled_patterns):
            if re.match(compiled_pattern, input_path):
                target_name = os.path.basename(input_path)
                target_path = os.path.join(directories[n], target_name)

                cls.check_target_directory(directories[n], create)

                if os.path.isfile(input_path):
                    copy_file(home_dir_to_absolute_path(input_path), home_dir_to_absolute_path(target_path), overwrite)
                    print('Successfully copied file: %s' % target_name)
                
                elif os.path.isdir(input_path):
                    copy_tree(home_dir_to_absolute_path(input_path), home_dir_to_absolute_path(target_path), overwrite)
                    print('Successfully copied directory: %s' % target_name)

                break

    @classmethod
    def check_target_directory(cls, directory, create):
        if os.path.isdir(home_dir_to_absolute_path(directory)):
            print('Target directory exists: %s' % directory)
            return
        else:
            if create:
                os.makedirs(directory)
                print('Target directory created: %s' % directory)
            else:
                sys.exit('Can\'t continue. Target directory does NOT exist and "create_directory" set to False: %s' %
                         directory)
