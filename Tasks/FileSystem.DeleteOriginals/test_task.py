#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import py
import os
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  delete_to_trash=False)

    assert isinstance(t, object)


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    original_file = tmpdir.join('test_file.txt')
    original_file.write('foo')

    symlink_to_original_file = tmpdir.join('0', 'files', 'test_file.txt')
    os.symlink('%s' % original_file, '%s' % symlink_to_original_file)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    assert original_file.check() is True

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  delete_to_trash=False)

    assert original_file.check() is False
