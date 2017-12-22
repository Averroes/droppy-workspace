#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from PIL import Image, ExifTags
from shutil import copyfile
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/image-rename-by-exif
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.rename_file(item_path, output_dir)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.rename_file(contained_file, output_sub_dir)

    @staticmethod
    def rename_file(input_file, output_dir):
        output_file_name = os.path.basename(input_file)

        try:
            input_image = Image.open(input_file)
            # noinspection PyProtectedMember
            for key, value in input_image._getexif().items():
                if key in ExifTags.TAGS:
                    if ExifTags.TAGS[key] == 'DateTimeOriginal':
                        output_file_name = value.replace(':', '')
                        output_file_name = output_file_name.replace(' ', '_')
                        output_file_name += '.jpg'
                        print('Renaming file "%s" to "%s"' % (os.path.basename(input_file), output_file_name))
        except Exception as err:
            print('Unable to read EXIF tag from file "%s"' % input_file)
            print(err)

        output_file = os.path.join(output_dir, output_file_name)
        copyfile(input_file, output_file)
