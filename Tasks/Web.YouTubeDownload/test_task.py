#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import pytest
import task


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir)

    assert isinstance(t, object)


def test_external_executable_na(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_dir='%s' % input_dir,
                      output_dir='%s' % output_dir,
                      youtubedl_executable='/this/path/does/not/exist')

    assert exc_info.type == SystemExit
