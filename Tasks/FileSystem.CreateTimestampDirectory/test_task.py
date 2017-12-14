#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
import task
import datetime

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'böok$ collection', 'pg5903.epub'),
                   os.path.join(files_dir, 'böok$ collection', 'vom gut und böse.epub')]
    name_pattern = '%Y-%m'

    t = task.Task(input_paths=input_paths,
                  output_dir='%s' % tmpdir,
                  name_pattern=name_pattern)

    d = datetime.datetime.now()
    year_month = d.strftime(name_pattern)

    assert tmpdir.join(year_month, 'pg5903.epub').check() is True
    assert tmpdir.join(year_month, 'vom gut und böse.epub').check() is True


def test_len_zero_name_pattern_arg(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir,
                      name_pattern='')

    assert exc_info.type == SystemExit
