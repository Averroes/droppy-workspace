#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from shell_tools import sanitize_file_path_for_shell


def test_sanitize_file_path_for_shell():
    input_string = '$ABC "def" `ghi`'
    output_string = sanitize_file_path_for_shell(file_path=input_string)

    assert ('\\$' in input_string) is False
    assert ('\\$' in output_string) is True

    assert ('\\"' in input_string) is False
    assert ('\\"' in output_string) is True

    assert ('\\`' in input_string) is False
    assert ('\\`' in output_string) is True
