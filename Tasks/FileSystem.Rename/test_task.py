#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  name='abc.txt')

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'my_textfile.txt'),
                   os.path.join(files_dir, 'some_subdir', 'sämple.md'),
                   os.path.join(files_dir, 'spécîal chär sübdir', 'another_file')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  name='néw_file name.txt')

    assert tmpdir.join('néw_file name.txt').check() is True
    assert tmpdir.join('néw_file name copy 1.txt').check() is True
    assert tmpdir.join('néw_file name copy 2.txt').check() is True


def test_passing_dirs(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir'),
                   os.path.join(files_dir, 'spécîal chär sübdir')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  name='néw_dir name')

    assert tmpdir.join('néw_dir name').check() is True
    assert tmpdir.join('néw_dir name copy 1').check() is True


def test_passing_files_and_dirs(tmpdir):
    input_paths = [os.path.join(files_dir, 'my_textfile.txt'),
                   os.path.join(files_dir, 'spécîal chär sübdir')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  name='néw name')

    assert tmpdir.join('néw name').check() is True
    assert tmpdir.join('néw name copy 1').check() is True
