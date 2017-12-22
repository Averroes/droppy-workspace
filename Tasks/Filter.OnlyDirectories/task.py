#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from distutils.dir_util import copy_tree


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filter-only-directories
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                print('Skipping file: %s' % item_path)

            elif os.path.isdir(item_path):
                copy_tree(item_path, os.path.join(output_dir, item_name))
