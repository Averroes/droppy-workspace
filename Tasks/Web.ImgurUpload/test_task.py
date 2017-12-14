#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import task


def test_init(tmpdir):
    t = task.Task(input_paths=[],
                  output_dir='%s' % tmpdir,
                  client_id='some invalid client id')

    assert isinstance(t, object)


def test_missing_client_id_arg(tmpdir):
    with pytest.raises(SystemExit) as exc_info:
        t = task.Task(input_paths=[],
                      output_dir='%s' % tmpdir)

    assert exc_info.type == SystemExit
