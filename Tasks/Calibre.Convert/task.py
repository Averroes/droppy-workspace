#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory
from shell_tools import sanitize_file_path_for_shell


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/calibre-convert
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        ebookconvert_exe = kwargs.get(str('executable'), '/Applications/calibre.app/Contents/MacOS/ebook-convert')
        extension = kwargs.get(str('extension'), 'mobi')

        # Check for required external executable.
        if not os.path.isfile(ebookconvert_exe):
            sys.exit('ebook-convert not found at "%s"' % ebookconvert_exe)

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.convert_book(item_path, output_dir, ebookconvert_exe, extension)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)

                os.makedirs(output_sub_dir)
                contained_files = get_file_paths_from_directory(item_path)

                for contained_file in contained_files:
                    self.convert_book(contained_file, output_sub_dir, ebookconvert_exe, extension)

    @staticmethod
    def convert_book(input_file, output_dir, ebookconvert_exe, extension):
        output_file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, output_file_name + '.' + extension)

        command = ebookconvert_exe
        command += ' "%s"' % sanitize_file_path_for_shell(input_file)
        command += ' "%s"' % sanitize_file_path_for_shell(output_file)

        print('Calling: %s' % command)

        exit_code = subprocess.call(command, shell=True)
        if exit_code > 0:
            sys.exit(exit_code)
