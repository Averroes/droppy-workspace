#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_dir=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    t = task.Task(input_dir=[os.path.join(files_dir, 'my_textfile.txt')],
                  output_dir='%s' % tmpdir)

    output_file_lines = codecs.open('%s' % tmpdir.join('my_textfile.txt'), encoding='utf-8', mode='r').readlines()
    assert len(output_file_lines) == 2
