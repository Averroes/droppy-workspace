#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from shutil import copyfile


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filter-by-extensions
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        extensions = kwargs.get(str('extensions'), ['txt', 'json', 'xml'])

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                full_output_path = (os.path.join(output_dir, item_name))
                self.check_and_copy(extensions, item_path, full_output_path)

            elif os.path.isdir(item_path):
                output_base = item_name
                os.makedirs(os.path.join(output_dir, output_base))

                for root, dirs, files in os.walk(item_path):
                    for d in dirs:
                        relative_path = root[len(item_path) + 1:]
                        os.makedirs(os.path.join(output_dir, output_base, relative_path, d))

                    for f in files:
                        relative_path = root[len(item_path) + 1:]
                        full_input_path = os.path.join(root, f)
                        full_output_path = os.path.join(output_dir, output_base, relative_path, f)

                        self.check_and_copy(extensions, full_input_path, full_output_path)

    @staticmethod
    def check_and_copy(extensions, full_input_path, full_output_path):
        file_name, file_extension = os.path.splitext(full_input_path)
        extensions_uppercased = [extension.upper() for extension in extensions]
        if file_extension.replace('.', '').upper() in extensions_uppercased:
            copyfile(full_input_path, full_output_path)
