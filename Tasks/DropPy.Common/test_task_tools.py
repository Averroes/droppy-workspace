#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import py
import shutil
from task_tools import get_original_paths, pass_input_to_output

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_get_original_paths(tmpdir):
    source_dir = tmpdir.join('-1')
    os.makedirs('%s' % source_dir)

    shutil.copyfile('%s' % files_dir.join('this_side_up.png'),
                    '%s' % source_dir.join('this_side_up.png'))

    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    os.symlink('%s' % source_dir.join('this_side_up.png'),
               '%s' % input_dir.join('this_side_up_0.png'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    return_value = get_original_paths(input_or_output_dir='%s' % output_dir)

    assert ('%s' % source_dir.join('this_side_up.png') in return_value) is True


def test_pass_input_to_output(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    shutil.copyfile('%s' % files_dir.join('pg5903.epub'),
                    '%s' % input_dir.join('pg5903.epub'))

    input_sub_dir = input_dir.join('foo')
    os.makedirs('%s' % input_sub_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    pass_input_to_output(input_dir='%s' % input_dir,
                         output_dir='%s' % output_dir)

    assert output_dir.join('pg5903.epub').check() is True
    assert output_dir.join('foo').check() is True
