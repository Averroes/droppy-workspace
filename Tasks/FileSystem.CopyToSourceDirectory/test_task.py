#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
from shutil import copyfile, copytree
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    original_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % original_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_paths=[],
                  output_dir='%s' % output_dir,
                  fallback_path='%s' % tmpdir)

    assert isinstance(t, object)


def test_unfilled_fallback_path_arg(tmpdir):
    original_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % original_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % output_dir)

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
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

    fallback_dir = tmpdir.join('fallback')
    os.makedirs('%s' % fallback_dir)

    t = task.Task(input_paths=['%s' % input_dir.join('this_side_up_0.png'),
                               '%s' % input_dir.join('äudio collection 0')],
                  output_dir='%s' % output_dir,
                  fallback_path='%s' % fallback_dir)

    assert source_dir.join('this_side_up_0.png').check() is True
    assert source_dir.join('äudio collection 0').check() is True
