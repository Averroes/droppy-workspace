#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
try:
    import Image
except ImportError:
    from PIL import Image
import pytest
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_dir=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_passing_files(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir', 'IMG_1248.JPG')]

    t = task.Task(input_dir=input_paths,
                  output_dir='%s' % tmpdir,
                  width=900,
                  height=200,
                  filter='nearest')

    resized_image = Image.open('%s' % tmpdir.join('IMG_1248.JPG'))
    width, height = resized_image.size

    assert width == 900
    assert height == 200


def test_invalid_filter_arg(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir', 'IMG_1248.JPG')]

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir=input_paths,
                      output_dir='%s' % tmpdir,
                      width=900,
                      height=200,
                      filter='this filter does not exist')

    assert exc_info.type == SystemExit
