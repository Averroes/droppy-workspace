#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_external_executable_na(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir,
                      ffmpeg_executable='/this/path/does/not/exist')

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    t = task.Task(input_paths=[os.path.join(files_dir, 'this_side_up.png')],
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('this_side_up.m4v').check() is True
