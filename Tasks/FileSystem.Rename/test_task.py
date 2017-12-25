#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import py
import pytest
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  name='abc.txt')

    assert isinstance(t, object)


def test_unfilled_fallback_path_arg(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir)

    assert exc_info.type == SystemExit


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    input_dir.join('my_textfile.txt').write('foo')
    input_dir.join('another file').write('bar')

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  name='néw_file name.txt')

    assert output_dir.join('néw_file name.txt').check() is True
    assert output_dir.join('néw_file name copy 1.txt').check() is True


def test_input_folder(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    os.makedirs('%s' % input_dir.join('some_subdir'))
    os.makedirs('%s' % input_dir.join('spécîal chär sübdir'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  name='néw_dir name')

    assert output_dir.join('néw_dir name').check() is True
    assert output_dir.join('néw_dir name copy 1').check() is True
