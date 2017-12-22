#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
import datetime

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import copy_file, copy_tree


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-create-timestamp-directory
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        name_pattern = kwargs.get(str('name_pattern'), '%Y-%m-%d_%H%M%S')

        # Check required argument.
        if len(name_pattern) == 0:
            sys.exit('No name_pattern passed')

        timestamp_dir = self.create_directory(output_dir, name_pattern)

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                copy_file(item_path, os.path.join(timestamp_dir, item_name), False)

            elif os.path.isdir(item_path):
                copy_tree(item_path, os.path.join(timestamp_dir, item_name), False)

    @staticmethod
    def create_directory(output_dir, name_pattern):
        try:
            d = datetime.datetime.now()
            timestamp_dir_name = d.strftime(name_pattern)
            timestamp_dir = os.path.join(output_dir, timestamp_dir_name)
            os.makedirs(timestamp_dir)
            print('Created directory "%s"' % timestamp_dir_name)
        except Exception as err:
            sys.exit('Unable to use name_pattern "%s", %s' % (name_pattern, err))

        return timestamp_dir
