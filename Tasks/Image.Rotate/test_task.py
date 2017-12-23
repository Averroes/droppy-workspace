#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
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
                  output_dir='%s' % tmpdir)

    original_image = Image.open(input_paths[0])
    original_width, original_height = original_image.size

    rotated_image = Image.open('%s' % tmpdir.join('IMG_1248.JPG'))
    new_width, new_height = rotated_image.size

    assert original_width == new_height
    assert original_height == new_width


def test_invalid_expand_arg(tmpdir):
    input_paths = [os.path.join(files_dir, 'some_subdir', 'IMG_1248.JPG')]

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir=input_paths,
                      output_dir='%s' % tmpdir,
                      expand=44)

    assert exc_info.type == SystemExit
