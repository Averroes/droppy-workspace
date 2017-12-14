#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def sanitize_file_path_for_shell(file_path):
    """
    Replace characters that are ok for the filesystem but have special meaning in the shell.
    It is assumed file_path is already passed in double quotes.
    """
    file_path_sanitized = file_path.replace('\\', '\\\\')
    file_path_sanitized = file_path_sanitized.replace('$', '\\$')
    file_path_sanitized = file_path_sanitized.replace('"', '\\"')
    file_path_sanitized = file_path_sanitized.replace('`', '\\`')
    return file_path_sanitized
