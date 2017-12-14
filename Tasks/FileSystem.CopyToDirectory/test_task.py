#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir,
                  directory='~')

    assert isinstance(t, object)


def test_unfilled_directory_arg(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir)

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'böok$ collection', 'pg5903.epub'),
                   os.path.join(files_dir, 'böok$ collection', 'vom gut und böse.epub')]

    t = task.Task(input_paths=input_paths,
                  output_dir='%s' % tmpdir,
                  directory='%s' % tmpdir.join('some other dir'),
                  create_directory=True)

    assert tmpdir.join('some other dir', 'pg5903.epub').check() is True
    assert tmpdir.join('some other dir', 'vom gut und böse.epub').check() is True


def test_passing_dir(tmpdir):
    input_paths = [os.path.join(files_dir, 'böok$ collection')]

    t = task.Task(input_paths=input_paths,
                  output_dir='%s' % tmpdir,
                  directory='%s' % tmpdir.join('some other dir'),
                  create_directory=True)

    assert tmpdir.join('some other dir', 'böok$ collection').check() is True
    assert tmpdir.join('some other dir', 'böok$ collection', 'pg5903.epub').check() is True
    assert tmpdir.join('some other dir', 'böok$ collection', 'vom gut und böse.epub').check() is True
