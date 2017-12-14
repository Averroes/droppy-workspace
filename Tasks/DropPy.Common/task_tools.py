#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from file_tools import copy_file, copy_tree


def get_original_paths(output_path):
    """
    Get the list of absolute paths of the files and folders that were originally dropped on DropPy.
    These files have not been copied to temp-dir/0/files but symlinked.
    """
    files_dir_path = os.path.abspath(os.path.join(output_path, os.pardir, '0', 'files'))
    original_paths = []
    for symlink_file in os.listdir(files_dir_path):
        symlink_path = os.path.join(files_dir_path, symlink_file)
        real_path = os.path.realpath(symlink_path)
        original_paths.append(real_path)
    return original_paths


def pass_input_to_output(input_paths, output_dir):
    """
    Copy all input files and folders to the output_dir without changing them.
    """
    for input_path in input_paths:
        target_name = os.path.basename(input_path)
        if os.path.isfile(input_path):
            copy_file(input_path, os.path.join(output_dir, target_name), False)
        elif os.path.isdir(input_path):
            copy_tree(input_path, os.path.join(output_dir, target_name), False)
