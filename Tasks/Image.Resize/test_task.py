#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
try:
    import Image
except ImportError:
    from PIL import Image
import py
import pytest
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
                  output_dir='%s' % output_dir,
                  width=900,
                  height=200,
                  filter='nearest')

    resized_image = Image.open('%s' % output_dir.join('IMG_1248.JPG'))
    width, height = resized_image.size

    assert width == 900
    assert height == 200


def test_invalid_filter_arg(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      width=900,
                      height=200,
                      filter='this filter does not exist')

    assert exc_info.type == SystemExit
