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


FILE_FORMATS_WITH_TRANSPARENCY = ['gif', 'png', 'xpm']


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/image-convert
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        extension = kwargs.get(str('extension'), 'png')
        background = kwargs.get(str('background'), [255, 255, 255])

        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.convert_file(input_path, output_dir, extension, background)

            elif os.path.isdir(input_path):
                output_sub_dir = os.path.join(output_dir, os.path.basename(input_path))
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(input_path)
                for contained_file in contained_files:
                    self.convert_file(contained_file, output_sub_dir, extension, background)

    @staticmethod
    def convert_file(input_file, output_dir, output_extension, bg_replacement):
        input_file_name, input_extension = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, input_file_name + '.' + output_extension)

        input_image = Image.open(input_file).convert('RGBA')  # always load with alpha channel

        # Replace transparency when converting from file formats that support it to ones that don't.
        if output_extension.lower() not in FILE_FORMATS_WITH_TRANSPARENCY:
            print('Replacing transparent parts with color %s.' % bg_replacement)
            bg_image = Image.new('RGBA', input_image.size, (bg_replacement[0], bg_replacement[1], bg_replacement[2]))

            non_transparent_image = Image.alpha_composite(bg_image, input_image)
            non_transparent_image = non_transparent_image.convert('RGB')

            non_transparent_image.save(output_file)
        else:
            input_image.save(output_file)
