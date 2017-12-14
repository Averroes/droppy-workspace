#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import task


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir,
                  server_address='localhost',
                  remote_path='/')

    assert isinstance(t, object)


def test_unfilled_server_address_arg(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir,
                      remote_path='/')

    assert exc_info.type == SystemExit


def test_unfilled_remote_path_arg(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir)

    assert exc_info.type == SystemExit


def test_external_executable_na(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir,
                      server_address='localhost',
                      executable='/this/path/does/not/exist/scp',
                      remote_path='/')

    assert exc_info.type == SystemExit
