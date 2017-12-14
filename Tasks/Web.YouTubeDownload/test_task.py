#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import pytest
import task

files_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'Test', 'files'))


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir)

    assert isinstance(t, object)


def test_external_executable_na(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir,
                      youtubedl_executable='/this/path/does/not/exist')

    assert exc_info.type == SystemExit


def test_passing_files(tmpdir):
    input_paths = ['%s' % tmpdir.join('youtube_urls.txt')]

    with codecs.open(input_paths[0], encoding='utf-8', mode='w') as file_handler:
        file_handler.write('https://www.youtube.com/watch?v=dJBLa2GmnXg\n')

    t = task.Task(input_paths=input_paths,
                  output_dir='%s' % tmpdir)

    assert len(tmpdir.listdir()) == 2
