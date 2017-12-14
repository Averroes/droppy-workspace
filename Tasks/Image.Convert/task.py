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
    Documentation: https://docs.droppyapp.com/tasks/image-convert
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        extension = kwargs.get(str('extension'), 'png')

        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.convert_file(input_path, output_dir, extension)

            elif os.path.isdir(input_path):
                output_sub_dir = os.path.join(output_dir, os.path.basename(input_path))
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(input_path)
                for contained_file in contained_files:
                    self.convert_file(contained_file, output_sub_dir, extension)

    @staticmethod
    def convert_file(input_file, output_dir, extension):
        output_file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, output_file_name + '.' + extension)

        input_image = Image.open(input_file)
        input_image.save(output_file)
