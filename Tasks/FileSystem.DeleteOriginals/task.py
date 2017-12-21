#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from shutil import rmtree
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from task_tools import get_original_paths, pass_input_to_output


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-delete-originals
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        delete_to_trash = kwargs.get(str('delete_to_trash'), True)

        # Process files and directories.
        original_paths = get_original_paths(output_dir)

        for original_path in original_paths:
            if os.path.isfile(original_path):
                self.delete_file(delete_to_trash, original_path)
            elif os.path.isdir(original_path):
                self.delete_tree(delete_to_trash, original_path)

        # Up to this point our Task has no output. Which means the next Task has no input to work with.
        # So we're re-using the previous Task's output, by passing it down.
        pass_input_to_output(input_paths, output_dir)

    @classmethod
    def delete_file(cls, delete_to_trash, file_path):
        if delete_to_trash:
            print('Moving file to Trash: %s' % file_path)
            cls.delete_to_trash(file_path)
        else:
            print('Removing file: %s' % file_path)
            os.remove(file_path)

    @classmethod
    def delete_tree(cls, delete_to_trash, directory_path):
        if delete_to_trash:
            print('Moving directory to Trash: %s' % directory_path)
            cls.delete_to_trash(directory_path)
        else:
            print('Removing directory: %s' % directory_path)
            rmtree(directory_path)

    @staticmethod
    def delete_to_trash(item_path):
        # Source: http://www.anthonysmith.me.uk/2008/01/08/moving-files-to-trash-from-the-mac-command-line/
        command = '/usr/bin/osascript -e "tell app \\\"Finder\\\" to move POSIX file \\\"%s\\\" to trash"' % item_path
        exit_code = subprocess.call(command, shell=True)
        if exit_code > 0:
            sys.exit(exit_code)
