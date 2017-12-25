#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
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

    images_dir = tmpdir.join('images')
    os.makedirs('%s' % images_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  patterns=[r'^.+\.png'],
                  directories=['%s' % images_dir])

    assert isinstance(t, object)


def test_unfilled_patterns_arg(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    images_dir = tmpdir.join('images')
    os.makedirs('%s' % images_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      directories=['%s' % images_dir])

    assert exc_info.type == SystemExit


def test_unfilled_directories_arg(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      patterns=[r'^.+\.png'])

    assert exc_info.type == SystemExit


def test_different_length_patterns_directories_args(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    images_dir = tmpdir.join('images')
    os.makedirs('%s' % images_dir)

    documents_dir = tmpdir.join('documents')
    os.makedirs('%s' % documents_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      patterns=[r'^.+\.png'],
                      directories=['%s' % images_dir,
                                   '%s' % documents_dir])

    assert exc_info.type == SystemExit


def test_input_file(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    shutil.copyfile('%s' % files_dir.join('pg5903.epub'),
                    '%s' % input_dir.join('pg5903.epub'))

    shutil.copyfile('%s' % files_dir.join('this_side_up.png'),
                    '%s' % input_dir.join('this_side_up.png'))

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    images_dir = tmpdir.join('images')
    os.makedirs('%s' % images_dir)

    documents_dir = tmpdir.join('documents')
    os.makedirs('%s' % documents_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  patterns=[r'^.+\.png',
                            r'^.+\.epub'],
                  directories=['%s' % images_dir,
                               '%s' % documents_dir])

    assert images_dir.join('pg5903.epub').check() is False
    assert images_dir.join('this_side_up.png').check() is True

    assert documents_dir.join('pg5903.epub').check() is True
    assert documents_dir.join('this_side_up.png').check() is False
