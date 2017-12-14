#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    original_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % original_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_paths=[],
                  output_dir='%s' % output_dir,
                  delete_to_trash=False)

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    original_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % original_dir)

    original_file = tmpdir.join('test_file.txt')
    with codecs.open('%s' % original_file, 'a'):
        os.utime('%s' % original_file, None)

    symlink_to_original_file = tmpdir.join('0', 'files', 'test_file.txt')
    os.symlink('%s' % original_file, '%s' % symlink_to_original_file)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    assert original_file.check() is True

    t = task.Task(input_paths=[],
                  output_dir='%s' % output_dir,
                  delete_to_trash=False)

    assert original_file.check() is False
