#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
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

    shutil.copyfile('%s' % files_dir.join('IMG_1248.JPG'),
                    '%s' % input_dir.join('IMG_1248.JPG'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert output_dir.join('20170914_102630.jpg').check() is True


def test_input_folder(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    input_sub_folder = input_dir.join('some subdir')
    os.makedirs('%s' % input_sub_folder)

    shutil.copyfile('%s' % files_dir.join('IMG_1248.JPG'),
                    '%s' % input_sub_folder.join('IMG_1248.JPG'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert output_dir.join('some subdir', '20170914_102630.jpg').check() is True
