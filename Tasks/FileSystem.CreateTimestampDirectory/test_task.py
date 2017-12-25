#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import py
import pytest
import shutil
import task
import datetime

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert isinstance(t, object)


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    shutil.copyfile('%s' % files_dir.join('pg5903.epub'),
                    '%s' % input_dir.join('pg5903.epub'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    name_pattern = '%Y-%m'

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  name_pattern=name_pattern)

    d = datetime.datetime.now()
    year_month = d.strftime(name_pattern)

    assert output_dir.join(year_month, 'pg5903.epub').check() is True


def test_len_zero_name_pattern_arg(tmpdir):
    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      name_pattern='')

    assert exc_info.type == SystemExit
