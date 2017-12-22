#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_dir=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_external_executable_na(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir=[],
                      output_dir='%s' % tmpdir,
                      flac_executable='/this/path/does/not/exist')

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'äudio collection', 'homer.flac')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('homer.mp3').check() is True


def test_passing_dir(tmpdir):
    input_paths = [os.path.join(files_dir, 'äudio collection')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('äudio collection', 'homer.mp3').check() is True
