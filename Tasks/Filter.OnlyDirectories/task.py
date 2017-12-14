#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from distutils.dir_util import copy_tree


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filter-only-directories
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                print('Skipping file: %s' % input_path)

            elif os.path.isdir(input_path):
                output_name = os.path.basename(input_path)
                copy_tree(input_path, os.path.join(output_dir, output_name))
