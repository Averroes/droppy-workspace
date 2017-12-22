#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import sys
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/image-ocr
    """
    def __init__(self, input_dir, output_dir, **kwargs):
        # Get keyword arguments.
        tesseract_exe = kwargs.get(str('executable'), '/usr/local/bin/tesseract')
        language = kwargs.get(str('language'), 'eng')
        boxes = kwargs.get(str('boxes'), False)
        config = kwargs.get(str('config'), '')

        # Check for required external executable.
        if not os.path.isfile(tesseract_exe):
            sys.exit('tesseract not found at "%s"' % tesseract_exe)

        # Process files and directories.
        for item_name in os.listdir(input_dir):
            item_path = os.path.join(input_dir, item_name)

            if os.path.isfile(item_path):
                self.run_ocr(item_path, output_dir, tesseract_exe, language, boxes, config)

            elif os.path.isdir(item_path):
                output_sub_dir = os.path.join(output_dir, item_name)
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(item_path)
                for contained_file in contained_files:
                    self.run_ocr(contained_file, output_sub_dir, tesseract_exe, language, boxes, config)

    @staticmethod
    def run_ocr(input_file, output_dir, tesseract_exe, language, boxes, config):
        output_file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, output_file_name + '.txt')

        input_image = Image.open(input_file)
        pytesseract.pytesseract.tesseract_cmd = tesseract_exe
        output_string = pytesseract.image_to_string(input_image, lang=language, boxes=boxes, config=config)

        with codecs.open(output_file, encoding='utf-8', mode='w') as file_handler:
            file_handler.write(output_string + '\n')
