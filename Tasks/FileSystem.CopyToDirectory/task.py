#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import copy_file, copy_tree
from task_tools import pass_input_to_output


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-copy-to-directory
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        directory = kwargs.get(str('directory'), '')
        create = kwargs.get(str('create_directory'), False)
        overwrite = kwargs.get(str('overwrite_existing'), False)

        # Check required argument.
        if len(directory) > 0:
            directory = os.path.expanduser(directory)
            self.check_target_directory(directory, create)
        else:
            sys.exit('No directory passed to copy to')

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                copy_file(item_path, os.path.join(directory, item_name), overwrite)

            elif os.path.isdir(item_path):
                copy_tree(item_path, os.path.join(directory, item_name), overwrite)

        # Up to this point our Task has no output. Which means the next Task has no input to work with.
        # So we're re-using the previous Task's output, by passing it down.
        pass_input_to_output(input_dir, output_dir)

    @staticmethod
    def check_target_directory(directory, create):
        if os.path.isdir(directory):
            print('Target directory exists: %s' % directory)
            return
        else:
            if create:
                os.makedirs(directory)
                print('Target directory created: %s' % directory)
            else:
                sys.exit('Can\'t continue. Target directory does NOT exist and "create_directory" set to False: %s' %
                         directory)
