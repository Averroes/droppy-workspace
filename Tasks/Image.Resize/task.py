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
    Documentation: https://docs.droppyapp.com/tasks/image-resize
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        width = kwargs.get(str('width'), 800)
        height = kwargs.get(str('height'), 600)
        image_filter = kwargs.get(str('filter'), 'antialias')

        # Check arguments.
        if image_filter == 'antialias':
            resample = Image.ANTIALIAS
        elif image_filter == 'box':
            resample = Image.BOX
        elif image_filter == 'bilinear':
            resample = Image.BILINEAR
        elif image_filter == 'hamming':
            resample = Image.HAMMING
        elif image_filter == 'bicubic':
            resample = Image.BICUBIC
        elif image_filter == 'nearest':
            resample = Image.NEAREST
        else:
            sys.exit('No valid filter passed')

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.resize_file(item_path, output_dir, width, height, resample)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.resize_file(contained_file, output_sub_dir, width, height, resample)

    @staticmethod
    def resize_file(input_file, output_dir, width, height, resample):
        output_file_name = os.path.basename(input_file)
        output_file = os.path.join(output_dir, output_file_name)

        input_image = Image.open(input_file)
        output_image = input_image.resize((width, height), resample)
        output_image.save(output_file)
