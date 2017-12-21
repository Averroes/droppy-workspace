#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
from shutil import copyfile
import datetime
from distutils.dir_util import copy_tree


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-rename
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        name = kwargs.get(str('name'), '')
        timestamp_prefix = kwargs.get(str('timestamp_prefix'), False)
        timestamp_pattern = kwargs.get(str('timestamp_pattern'), '%Y-%m-%d_%H%M%S')

        # Check required argument.
        if len(name) == 0:
            sys.exit('No new name provided')

        # Process files and directories.
        for input_path in input_paths:
            if timestamp_prefix:
                d = datetime.datetime.now()
                timestamp = d.strftime(timestamp_pattern)
            else:
                timestamp = ''

            new_output_path = self.get_path_counter(output_dir, timestamp + name)

            if os.path.isfile(input_path):
                copyfile(input_path, new_output_path)
            elif os.path.isdir(input_path):
                copy_tree(input_path, new_output_path)

    @staticmethod
    def get_path_counter(output_dir, name):
        path_without_counter = os.path.join(output_dir, name)

        if os.path.isfile(path_without_counter) or os.path.isdir(path_without_counter):

            counter = 1
            no_ext, ext = os.path.splitext(name)
            while True:
                name_with_counter = no_ext + ' copy %s' % counter + ext
                path_with_counter = os.path.join(output_dir, name_with_counter)
                if os.path.isfile(path_with_counter) or os.path.isdir(path_with_counter):
                    counter += 1
                else:
                    return path_with_counter
        else:
            return path_without_counter
