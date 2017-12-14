#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir')]

    t = task.Task(input_paths=input_paths,
                  output_dir='%s' % tmpdir,
                  utis=['files'])

    assert isinstance(t, object)
