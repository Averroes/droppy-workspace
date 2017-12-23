#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from shell_tools import sanitize_file_path_for_shell
from task_tools import pass_input_to_output


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-scp-upload
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        server_address = kwargs.get(str('server_address'), '')
        remote_path = kwargs.get(str('remote_path'), '')
        username = kwargs.get(str('username'), '')
        scp_exe = kwargs.get(str('scp_executable'), '/usr/bin/scp')

        # Check for required arguments.
        if len(server_address) == 0:
            sys.exit('No server_address passed')
        if len(remote_path) == 0:
            sys.exit('No remote_path passed')
        if len(username) == 0:
            sys.exit('No username passed')

        # Check for required external executable.
        if not os.path.isfile(scp_exe):
            sys.exit('scp not found at "%s"' % scp_exe)

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)
            self.upload_files(item_path, scp_exe, username, server_address, remote_path)

        # Up to this point our Task has no output. Which means the next Task has no input to work with.
        # So we're re-using the previous Task's output, by passing it down.
        pass_input_to_output(input_dir, output_dir)

    @staticmethod
    def upload_files(input_file, scp_exe, username, server_address, remote_path):
        command = scp_exe
        command += ' -r'
        command += ' -o StrictHostKeyChecking=no'
        command += ' "%s"' % sanitize_file_path_for_shell(input_file)
        command += ' %s@%s:%s' % (username, server_address, remote_path)

        print('Calling: %s' % command)

        exit_code = subprocess.call(command, shell=True)
        if exit_code > 0:
            sys.exit(exit_code)
