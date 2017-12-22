#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from file_tools import copy_file, copy_tree


def get_original_paths(input_or_output_dir):
    """
    Get the list of absolute paths of the files and folders that were originally dropped on DropPy.
    These files have NOT been copied to temp-dir/0/files but SYMLINKED.
    """
    files_dir_path = os.path.abspath(os.path.join(input_or_output_dir, os.pardir, '0', 'files'))
    original_paths = []
    for symlink_file in os.listdir(files_dir_path):
        symlink_path = os.path.join(files_dir_path, symlink_file)
        real_path = os.path.realpath(symlink_path)
        original_paths.append(real_path)
    return original_paths


def pass_input_to_output(input_dir, output_dir):
    """
    Copy all the files and folders in the input_dir to the output_dir without changing them.
    """
    for item_name in os.listdir(input_dir):
        item_path = os.path.join(input_dir, item_name)

        if os.path.isfile(item_path):
            copy_file(item_path, os.path.join(output_dir, item_name), False)
        elif os.path.isdir(item_path):
            copy_tree(item_path, os.path.join(output_dir, item_name), False)
