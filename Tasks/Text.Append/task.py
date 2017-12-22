#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory, touch_file


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/text-append
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        target_file = kwargs.get(str('target_file'), '')

        # Check required argument.
        if len(target_file) > 0:
            target_file = os.path.expanduser(target_file)
            print('Appending to "%s".' % target_file)
            if not os.path.isfile(target_file):
                touch_file(target_file)
        else:
            sys.exit('No target_file passed to append to')

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.append_to_file(item_path, target_file)

            elif os.path.isdir(item_path):
                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.append_to_file(contained_file, target_file)

    @staticmethod
    def append_to_file(input_file, target_file):
        with codecs.open(target_file, encoding='utf-8', mode='a') as target_file_handler:
            with codecs.open(input_file, encoding='utf-8', mode='r') as input_file_handler:
                target_file_handler.write('\n')
                for line in input_file_handler.readlines():
                    target_file_handler.write(line)
