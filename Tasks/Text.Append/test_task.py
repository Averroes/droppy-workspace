#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import pytest
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_dir=[],
                  output_dir='%s' % tmpdir,
                  target_file='%s' % tmpdir.join('output.txt'))

    assert isinstance(t, object)


def test_unfilled_target_file_arg(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir=[],
                      output_dir='%s' % tmpdir)

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'my_textfile.txt'),
                   os.path.join(files_dir, 'täxt datei.txt')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  target_file='%s' % tmpdir.join('output.txt'))

    assert tmpdir.join('output.txt').check() is True

    output_file_lines = codecs.open('%s' % tmpdir.join('output.txt'), encoding='utf-8', mode='r').readlines()
    assert len(output_file_lines) == 5
