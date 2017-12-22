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
                  extensions=['txt'])

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'my_textfile.txt'),
                   os.path.join(files_dir, 'this_side_up.png'),
                   os.path.join(files_dir, 'some_subdir', 'sämple.md'),
                   os.path.join(files_dir, 'spécîal chär sübdir', 'another_file')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  extensions=['txt', 'md'])

    assert tmpdir.join('my_textfile.txt').check() is True
    assert tmpdir.join('this_side_up.png').check() is False
    assert tmpdir.join('sämple.md').check() is True
    assert tmpdir.join('another_file').check() is False


def test_passing_dirs(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir'),
                   os.path.join(files_dir, 'spécîal chär sübdir')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  extensions=['txt', 'md'])

    assert tmpdir.join('some_subdir', 'sämple.md').check() is True
    assert tmpdir.join('spécîal chär sübdir').check() is True
    assert tmpdir.join('spécîal chär sübdir', 'another_file').check() is False


def test_passing_files_and_dirs(tmpdir):
    input_paths = [os.path.join(files_dir, 'my_textfile.txt'),
                   os.path.join(files_dir, 'this_side_up.png'),
                   os.path.join(files_dir, 'spécîal chär sübdir'),
                   os.path.join(files_dir, 'some_subdir')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  extensions=['txt', 'md'])

    assert tmpdir.join('my_textfile.txt').check() is True
    assert tmpdir.join('this_side_up.png').check() is False
    assert tmpdir.join('spécîal chär sübdir', 'another_file').check() is False
    assert tmpdir.join('some_subdir', 'sämple.md').check() is True
