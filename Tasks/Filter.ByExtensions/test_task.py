#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import py
import task

files_dir = py.path.local(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  extensions=['txt'])

    assert isinstance(t, object)


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    input_dir.join('my_textfile.txt').write('foo')
    input_dir.join('another file').write('bat')

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % tmpdir,
                  extensions=['txt'])

    assert tmpdir.join('my_textfile.txt').check() is True
    assert tmpdir.join('another file').check() is False


def test_input_dir(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    input_sub_dir = input_dir.join('some subdir')
    os.makedirs('%s' % input_sub_dir)
    input_sub_dir.join('my_textfile.txt').write('foo')
    input_sub_dir.join('another file').write('bat')

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % tmpdir,
                  extensions=['txt', 'md'])

    assert tmpdir.join('some subdir', 'my_textfile.txt').check() is True
    assert tmpdir.join('some subdir', 'another file').check() is False
