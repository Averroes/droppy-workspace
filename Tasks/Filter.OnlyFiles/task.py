#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from shutil import copyfile


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filter-only-files
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                output_file_name = os.path.basename(input_path)
                output_file = os.path.join(output_dir, output_file_name)
                copyfile(input_path, output_file)
            
            elif os.path.isdir(input_path):
                print('Skipping directory: %s' % input_path)
