#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir', 'sämple.md')]

    t = task.Task(input_paths=input_paths,
                  output_dir='%s' % tmpdir)

    output_file = tmpdir.join('sämple.md')
    lines = codecs.open('%s' % output_file, encoding='utf-8', mode='r').readlines()

    assert lines[0] == '# Table of Contents\n'
