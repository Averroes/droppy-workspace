#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import py
import os
import shutil
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert isinstance(t, object)


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    shutil.copyfile('%s' % files_dir.join('sämple.md'),
                    '%s' % input_dir.join('sämple.md'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  section_start_regex=r'^### An h3 header ###$')

    original_file_lines = codecs.open('%s' % input_dir.join('sämple.md'), encoding='utf-8', mode='r').readlines()
    assert '### An h3 header ###\n' in original_file_lines

    changed_file_lines = codecs.open('%s' % output_dir.join('sämple.md'), encoding='utf-8', mode='r').readlines()
    assert '### An h3 header ###\n' not in changed_file_lines
