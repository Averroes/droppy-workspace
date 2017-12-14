#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import distutils.dir_util
import os
import shutil
import sys


def touch_file(file_path):
    """
    Create a new empty file at file_path.
    """
    parent_dir = os.path.abspath(os.path.join(file_path, os.pardir))
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)
    with codecs.open(file_path, 'a'):
        os.utime(file_path, None)


def copy_file(input_file, output_file, overwrite=False):
    """
    Helper function to copy a file that adds an overwrite parameter.
    """
    if os.path.isfile(output_file):
        if overwrite:
            print('File exists, overwriting')
            shutil.copyfile(input_file, output_file)
        else:
            sys.exit('File exists, unable to continue: %s' % output_file)
    else:
        shutil.copyfile(input_file, output_file)


def copy_tree(input_dir, output_dir, overwrite=False):
    """
    Helper function to copy a directory tree that adds an overwrite parameter.
    """
    if os.path.isdir(output_dir):
        if overwrite:
            print('Directory exists, overwriting')
            distutils.dir_util.copy_tree(input_dir, output_dir)
        else:
            sys.exit('Directory exists, unable to continue: %s' % output_dir)
    else:
        distutils.dir_util.copy_tree(input_dir, output_dir)


def get_file_paths_from_directory(dir_path):
    """
    Walk a directory and create a list of all contained file_paths in all sub-directories.
    """
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            file_paths.append(os.path.join(root, f))
    return file_paths


def home_dir_to_absolute_path(file_path):
    """
    Expand the ~ in file_path to its absolute path.
    """
    return os.path.expanduser(file_path)
