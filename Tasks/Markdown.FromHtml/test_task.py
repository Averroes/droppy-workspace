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
    input_paths = [os.path.join(files_dir, 'sämple.html')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('sämple.md').check() is True
    assert os.path.getsize('%s' % tmpdir.join('sämple.md')) > 15000
