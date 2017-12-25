#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import task


def test_input_empty(tmpdir):
    input_dir = tmpdir.join('0')
    os.makedirs('%s' % input_dir)

    files_dir = input_dir.join('files')
    os.makedirs('%s' % files_dir)

    output_dir = tmpdir.join('1')
    os.makedirs('%s' % output_dir)

    t = task.Task(input_dir='%s' % input_dir,
                  output_dir='%s' % output_dir,
                  utis=['files'])

    assert isinstance(t, object)
