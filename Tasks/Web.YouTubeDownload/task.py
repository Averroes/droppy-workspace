#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import subprocess
import sys


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/web-youtube-download
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        youtubedl_exe = kwargs.get(str('youtubedl_executable'), '/usr/local/bin/youtube-dl')
        output_file_pattern = kwargs.get(str('output_file_pattern'), '%(title)s.%(ext)s')
        other_args = kwargs.get(str('other_args'), '')

        # Check for required external executable.
        if not os.path.isfile(youtubedl_exe):
            sys.exit('youtube-dl not found at "%s"' % youtubedl_exe)

        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.download_file(input_path, output_dir, youtubedl_exe, output_file_pattern, other_args)

            elif os.path.isdir(input_path):
                print('Skipping directory: %s' % input_path)

    @staticmethod
    def download_file(input_file, output_dir, youtubedl_exe, file_name_pattern, other_args):
        with codecs.open(input_file, encoding='utf-8', mode='r') as file_handler:
            for download_url in file_handler.readlines():

                command = youtubedl_exe
                command += ' --abort-on-error'
                command += ' --quiet'
                if len(other_args) > 0:
                    command += ' %s' % other_args
                command += ' --output "%s"' % (output_dir + os.sep + file_name_pattern)
                command += ' "%s"' % download_url

                print('Calling: %s' % command)

                exit_code = subprocess.call(command, shell=True)
                if exit_code > 0:
                    sys.exit(exit_code)
