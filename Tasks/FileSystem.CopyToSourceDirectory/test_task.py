#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import py
import pytest
import shutil
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  fallback_path='%s' % tmpdir)

    assert isinstance(t, object)


def test_unfilled_fallback_path_arg(tmpdir):
    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir)

    assert exc_info.type == SystemExit


def test_input_file(tmpdir):
    source_dir = tmpdir.join('-1')
    os.makedirs('%s' % source_dir)

    shutil.copyfile('%s' % files_dir.join('pg5903.epub'),
                    '%s' % source_dir.join('pg5903.epub'))

    input_dir = tmpdir.join('0', 'files')
    os.makedirs('%s' % input_dir)

    os.symlink('%s' % source_dir.join('pg5903.epub'),
               '%s' % input_dir.join('pg5903_0.epub'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    fallback_dir = tmpdir.join('fallback')
    os.makedirs('%s' % fallback_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  fallback_path='%s' % fallback_dir)

    assert source_dir.join('pg5903_0.epub').check() is True
