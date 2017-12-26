#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import py
import os
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

    file_one = input_dir.join('foo.txt')
    file_one.write('baz\n')

    file_two = input_dir.join('bar.txt')
    file_two.write('bar\n\n\n\n\nfoo')

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    output_file_one_lines = codecs.open('%s' % output_dir.join('foo.txt'), encoding='utf-8', mode='r').readlines()
    assert len(output_file_one_lines) == 1

    output_file_two_lines = codecs.open('%s' % output_dir.join('bar.txt'), encoding='utf-8', mode='r').readlines()
    assert len(output_file_two_lines) == 3
