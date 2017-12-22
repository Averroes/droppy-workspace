#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/macos-open-files-in-app
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        app_name = kwargs.get(str('app_name'), '')

        # Check for required arguments.
        if len(app_name) == 0:
            sys.exit('No app_name passed')

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)
            self.open_file(item_path, app_name)

    @staticmethod
    def open_file(input_path, app_name):
        command = '/usr/bin/osascript -e "tell app \\\"%s\\\" to open POSIX file \\\"%s\\\""' % (app_name, input_path)

        print('Calling: %s' % command)

        exit_code = subprocess.call(command, shell=True)
        if exit_code > 0:
            sys.exit(exit_code)
