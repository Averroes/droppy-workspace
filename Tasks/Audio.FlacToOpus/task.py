#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import subprocess
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory
from shell_tools import sanitize_file_path_for_shell


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/audio-flac-to-opus
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        opusenc_exe = kwargs.get(str('lopusenc_executable'), '/usr/local/bin/opusenc')
        bitrate = kwargs.get(str('bitrate'), '80')

        # Check for required external executable.
        if not os.path.isfile(opusenc_exe):
            sys.exit('opusenc not found at "%s"' % opusenc_exe)

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.transcode_file(item_path, output_dir, opusenc_exe, bitrate)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)

                os.makedirs(output_sub_dir)
                contained_files = get_file_paths_from_directory(item_path)

                for contained_file in contained_files:
                    self.transcode_file(contained_file, output_sub_dir, opusenc_exe, bitrate)

    @staticmethod
    def transcode_file(input_file, output_dir, opusenc_exe, bitrate):
        output_file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, output_file_name + '.opus')

        # Transcoding flac to opus via opusenc.
        command = '%s --bitrate %s --discard-pictures ' % (opusenc_exe, bitrate)
        command += '"%s" "%s"' % (sanitize_file_path_for_shell(input_file),
                                  sanitize_file_path_for_shell(output_file))

        print('Calling: %s' % command)

        exit_code = subprocess.call(command, shell=True)
        if exit_code > 0:
            sys.exit(exit_code)
