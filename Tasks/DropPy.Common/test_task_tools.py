#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from shutil import copyfile, copytree
from task_tools import get_original_paths, pass_input_to_output

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_get_original_paths(tmpdir):
    source_dir = tmpdir.join('-1')
    os.makedirs('%s' % source_dir)

    copyfile(os.path.join(files_dir, 'this_side_up.png'), '%s' % source_dir.join('this_side_up.png'))
    copytree(os.path.join(files_dir, 'äudio collection'), '%s' % source_dir.join('äudio collection'))

    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    os.symlink('%s' % source_dir.join('this_side_up.png'), '%s' % input_dir.join('this_side_up_0.png'))
    os.symlink('%s' % source_dir.join('äudio collection'), '%s' % input_dir.join('äudio collection 0'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    return_value = get_original_paths(output_path='%s' % output_dir)

    assert ('%s' % source_dir.join('this_side_up.png') in return_value) is True
    assert ('%s' % source_dir.join('äudio collection') in return_value) is True


def test_pass_input_to_output(tmpdir):
    pass_input_to_output(input_paths=[os.path.join(files_dir, 'some_subdir', 'IMG_1248.JPG'),
                                      os.path.join(files_dir, 'äudio collection')],
                         output_dir='%s' % tmpdir)

    assert tmpdir.join('IMG_1248.JPG').check() is True
    assert tmpdir.join('äudio collection').check() is True
