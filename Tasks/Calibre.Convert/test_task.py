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
                      ebookconvert_executable='/this/path/does/not/exist')

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'böok$ collection', 'pg5903.epub'),
                   os.path.join(files_dir, 'böok$ collection', 'vom gut und böse.epub')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('pg5903.mobi').check() is True
    assert tmpdir.join('vom gut und böse.mobi').check() is True


def test_passing_dir(tmpdir):
    input_paths = [os.path.join(files_dir, 'böok$ collection')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir)

    assert tmpdir.join('böok$ collection', 'pg5903.mobi').check() is True
    assert tmpdir.join('böok$ collection', 'vom gut und böse.mobi').check() is True
