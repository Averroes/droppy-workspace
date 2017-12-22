#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
from shutil import copyfile, copytree
from file_tools import touch_file, copy_file, copy_tree, get_file_paths_from_directory

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_touch_file(tmpdir):
    touched_file = tmpdir.join('my_file.txt')
    assert touched_file.check() is False

    touch_file('%s' % touched_file)
    assert touched_file.check() is True


def test_copy_file(tmpdir):
    input_dir = tmpdir.join('input')
    os.makedirs('%s' % input_dir)
    copyfile(os.path.join(files_dir, 'this_side_up.png'), '%s' % input_dir.join('this_side_up.png'))

    output_dir = tmpdir.join('target')
    os.makedirs('%s' % output_dir)

    copy_file(input_file='%s' % input_dir.join('this_side_up.png'),
              output_file='%s' % output_dir.join('this_side_up.png'))

    assert output_dir.join('this_side_up.png').check() is True


def test_copy_file_overwrite_false(tmpdir):
    input_dir = tmpdir.join('input')
    os.makedirs('%s' % input_dir)
    copyfile(os.path.join(files_dir, 'this_side_up.png'), '%s' % input_dir.join('this_side_up.png'))

    output_dir = tmpdir.join('target')
    os.makedirs('%s' % output_dir)
    copyfile(os.path.join(files_dir, 'this_side_up.png'), '%s' % output_dir.join('this_side_up.png'))

    with pytest.raises(SystemExit) as exc_info:
        copy_file(input_file='%s' % input_dir.join('this_side_up.png'),
                  output_file='%s' % output_dir.join('this_side_up.png'),
                  overwrite=False)

    assert exc_info.type == SystemExit


def test_copy_file_overwrite_true(tmpdir):
    input_dir = tmpdir.join('input')
    os.makedirs('%s' % input_dir)
    copyfile(os.path.join(files_dir, 'this_side_up.png'), '%s' % input_dir.join('this_side_up.png'))

    output_dir = tmpdir.join('target')
    os.makedirs('%s' % output_dir)
    copyfile(os.path.join(files_dir, 'this_side_up.png'), '%s' % output_dir.join('this_side_up.png'))

    copy_file(input_file='%s' % input_dir.join('this_side_up.png'),
              output_file='%s' % output_dir.join('this_side_up.png'),
              overwrite=True)

    assert output_dir.join('this_side_up.png').check() is True


def test_copy_tree(tmpdir):
    input_dir = tmpdir.join('input')
    os.makedirs('%s' % input_dir)
    copytree(os.path.join(files_dir, 'böok$ collection'), '%s' % input_dir.join('böok$ collection'))

    output_dir = tmpdir.join('target')
    os.makedirs('%s' % output_dir)

    copy_tree(input_dir='%s' % input_dir.join('böok$ collection'),
              output_dir='%s' % output_dir.join('böok$ collection'))

    assert output_dir.join('böok$ collection').check() is True
    assert output_dir.join('böok$ collection', 'pg5903.epub').check() is True


def test_copy_tree_overwrite_false(tmpdir):
    input_dir = tmpdir.join('input')
    os.makedirs('%s' % input_dir)
    copytree(os.path.join(files_dir, 'böok$ collection'), '%s' % input_dir.join('böok$ collection'))

    output_dir = tmpdir.join('target')
    os.makedirs('%s' % output_dir)
    copytree(os.path.join(files_dir, 'böok$ collection'), '%s' % output_dir.join('böok$ collection'))

    with pytest.raises(SystemExit) as exc_info:
        copy_tree(input_dir='%s' % input_dir.join('böok$ collection'),
                  output_dir='%s' % output_dir.join('böok$ collection'),
                  overwrite=False)

    assert exc_info.type == SystemExit


def test_copy_tree_overwrite_true(tmpdir):
    input_dir = tmpdir.join('input')
    os.makedirs('%s' % input_dir)
    copytree(os.path.join(files_dir, 'böok$ collection'), '%s' % input_dir.join('böok$ collection'))

    output_dir = tmpdir.join('target')
    os.makedirs('%s' % output_dir)
    copytree(os.path.join(files_dir, 'böok$ collection'), '%s' % output_dir.join('böok$ collection'))

    copy_tree(input_dir='%s' % input_dir.join('böok$ collection'),
              output_dir='%s' % output_dir.join('böok$ collection'),
              overwrite=True)

    assert output_dir.join('böok$ collection').check() is True
    assert output_dir.join('böok$ collection', 'pg5903.epub').check() is True


def test_get_file_paths_from_directory():
    return_value = get_file_paths_from_directory(dir_path=files_dir)
    assert (os.path.join(files_dir, 'my_textfile.txt') in return_value) is True
    assert (os.path.join(files_dir, 'some_subdir', 'IMG_1248.JPG') in return_value) is True
