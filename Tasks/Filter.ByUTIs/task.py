#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from distutils.dir_util import copy_tree


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filter-by-utis
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        utis = kwargs.get(str('utis'), ['files'])
        flatten_dir = kwargs.get(str('flatten_dir'), True)

        # Process directories.
        for input_path in input_paths:
            if os.path.basename(input_path) in utis:
                if flatten_dir:
                    print('Copying files from: %s' % os.path.basename(input_path))
                    copy_tree(input_path, output_dir)
                else:
                    print('Copying directory:  %s' % os.path.basename(input_path))
                    target_name = os.path.basename(input_path)
                    copy_tree(input_path, os.path.join(output_dir, target_name))
            else:
                print('Skipping directory: %s' % os.path.basename(input_path))
