#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import py
import pytest
import os
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  target_file='%s' % tmpdir.join('output.txt'))

    assert isinstance(t, object)


def test_unfilled_target_file_arg(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir)

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    file_one = input_dir.join('foo.txt')
    file_one.write('baz\n')
    file_two = input_dir.join('bar.txt')
    file_two.write('bar\n')

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  target_file='%s' % tmpdir.join('output.txt'))

    assert tmpdir.join('output.txt').check() is True

    output_file_lines = codecs.open('%s' % tmpdir.join('output.txt'), encoding='utf-8', mode='r').readlines()
    assert len(output_file_lines) == 4
