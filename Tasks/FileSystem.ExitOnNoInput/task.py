#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from task_tools import pass_input_to_output


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/filesystem-exit-on-no-input
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Check if there are files or folders in the input_dir.
        if len(os.listdir(input_dir)) == 0:
            sys.exit('No files or folders in input_dir. The previous Task wrote nothing to its output_dir.')
        else:
            # Up to this point our Task has no output. Which means the next Task has no input to work with.
            # So we're re-using the previous Task's output, by passing it down.
            pass_input_to_output(input_dir, output_dir)
