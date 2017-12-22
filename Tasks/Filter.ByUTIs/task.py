#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from distutils.dir_util import copy_tree


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filter-by-utis
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        utis = kwargs.get(str('utis'), ['files'])
        flatten_dir = kwargs.get(str('flatten_dir'), True)

        # Process directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if item_name in utis:
                if flatten_dir:
                    print('Copying files from: %s' % item_name)
                    copy_tree(item_path, output_dir)
                else:
                    print('Copying directory:  %s' % item_name)
                    copy_tree(item_path, os.path.join(output_dir, item_name))
            else:
                print('Skipping directory: %s' % item_name)
