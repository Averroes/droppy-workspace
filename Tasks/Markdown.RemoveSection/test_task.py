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
    input_paths = [os.path.join(files_dir, 'some_subdir', 'sämple.md')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  section_start_regex=r'^### An h3 header ###$')

    original_file_lines = codecs.open('%s' % input_paths[0], encoding='utf-8', mode='r').readlines()
    assert '### An h3 header ###\n' in original_file_lines

    changed_file_lines = codecs.open('%s' % tmpdir.join('sämple.md'), encoding='utf-8', mode='r').readlines()
    assert '### An h3 header ###\n' not in changed_file_lines
