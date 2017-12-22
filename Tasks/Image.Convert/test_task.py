#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_dir=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir', 'IMG_1248.JPG'),
                   os.path.join(files_dir, 'this_side_up.png')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('IMG_1248.png').check() is True
    assert tmpdir.join('this_side_up.png').check() is True
