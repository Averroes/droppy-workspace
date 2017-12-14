#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
try:
    import Image
except ImportError:
    from PIL import Image
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/image-rotate
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        degrees = kwargs.get(str('degrees'), 90.0)
        expand_arg = kwargs.get(str('expand'), True)

        # Check arguments.
        if expand_arg is True:
            expand = 1
        elif expand_arg is False:
            expand = 0
        else:
            sys.exit('Argument expand invalid')

        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.rotate_file(input_path, output_dir, degrees, expand)

            elif os.path.isdir(input_path):
                output_sub_dir = os.path.join(output_dir, os.path.basename(input_path))
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(input_path)
                for contained_file in contained_files:
                    self.rotate_file(contained_file, output_sub_dir, degrees, expand)

    @staticmethod
    def rotate_file(input_file, output_dir, degrees, expand):
        output_file_name = os.path.basename(input_file)
        output_file = os.path.join(output_dir, output_file_name)

        input_image = Image.open(input_file)
        output_image = input_image.rotate(degrees, expand=expand)
        output_image.save(output_file)
