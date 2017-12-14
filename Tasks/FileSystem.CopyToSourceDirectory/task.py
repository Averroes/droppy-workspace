#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import copy_file, copy_tree, home_dir_to_absolute_path
from task_tools import get_original_paths, pass_input_to_output


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-copy-to-source-directory
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        overwrite = kwargs.get(str('overwrite_existing'), False)
        fallback_path = kwargs.get(str('fallback_path'), '')

        # Process files and directories.
        original_paths = get_original_paths(output_dir)
        parent_path = self.get_parent_path(original_paths, fallback_path)

        for input_path in input_paths:
            target_name = os.path.basename(input_path)
            target_path = os.path.join(parent_path, target_name)

            if os.path.isfile(input_path):
                copy_file(input_path, target_path, overwrite)
            elif os.path.isdir(input_path):
                copy_tree(input_path, target_path, overwrite)

        # Up to this point our Task has no output. Which means the next Task has no input to work with.
        # So we're re-using the previous Task's output, by passing it down.
        pass_input_to_output(input_paths, output_dir)

    @staticmethod
    def get_parent_path(file_paths, fallback_path):
        parent_paths = []
        for file_path in file_paths:
            parent_path = os.path.abspath(os.path.join(file_path, os.pardir))
            if parent_path not in parent_paths:
                parent_paths.append(parent_path)

        if len(parent_paths) == 1:
            print('Source directory: %s' % parent_paths[0])
            return parent_paths[0]
        elif len(parent_paths) > 1:
            if fallback_path != '':
                fallback_path_abs = home_dir_to_absolute_path(fallback_path)
                print('Files originate from multiple directories. Using fallback path: %s' % fallback_path_abs)
                return fallback_path_abs
            else:
                sys.exit('Can\'t continue, files originate from multiple directories: %s' % parent_paths)
        else:
            if fallback_path != '':
                fallback_path_abs = home_dir_to_absolute_path(fallback_path)
                print('No parent paths found. Using fallback path: %s' % fallback_path_abs)
                return fallback_path_abs
            else:
                sys.exit('No parent paths found. Can\'t continue, no fallback path provided.')
