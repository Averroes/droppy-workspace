#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import os
import sys
import re

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


H1_SETEX_STYLE_REGEX = re.compile(r'^-+$')
H2_SETEX_STYLE_REGEX = re.compile(r'^=+$')
ATX_STYLE_REGEX = re.compile(r'^#{1,6} .*$')


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/markdown-add-toc
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        toc_header = kwargs.get(str('toc_header'), '# Table of Contents')

        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.add_toc(input_path, output_dir, toc_header)

            elif os.path.isdir(input_path):
                output_sub_dir = os.path.join(output_dir, os.path.basename(input_path))
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(input_path)
                for contained_file in contained_files:
                    self.add_toc(contained_file, output_sub_dir, toc_header)

    def add_toc(self, input_file, output_dir, toc_header):
        headers = []
        previous_line_content = ''

        # Parse source file.
        with codecs.open(input_file, encoding='utf-8', mode='r') as input_file_handler:
            inside_code_block = False
            for line in input_file_handler:
                # Skip fenced code blocks.
                if inside_code_block:
                    if line.startswith('```') or line.startswith('~~~'):
                        # We were in a code block but this line ended it, toggle mode and continue with next line.
                        inside_code_block = False
                        continue
                    else:
                        # We are still in a code block, continue with next line.
                        continue
                else:
                    if line.startswith('```') or line.startswith('~~~'):
                        # We are now in a code block, toggle mode and continue with next line.
                        inside_code_block = True
                        continue

                # Ignore lines indented by tab or 4x spaces.
                if line.startswith('\t') or line.startswith('    '):
                    continue

                # Detect the two types of headers.
                header = None
                if H1_SETEX_STYLE_REGEX.match(line):
                    header, previous_line_content = self.get_header(kind='setex',
                                                                    previous_line_content=previous_line_content,
                                                                    text=previous_line_content.strip(),
                                                                    level=1)
                elif H2_SETEX_STYLE_REGEX.match(line):
                    header, previous_line_content = self.get_header(kind='setex',
                                                                    previous_line_content=previous_line_content,
                                                                    text=previous_line_content.strip(),
                                                                    level=2)
                elif ATX_STYLE_REGEX.match(line):
                    header, previous_line_content = self.get_header(kind='atx',
                                                                    previous_line_content=previous_line_content,
                                                                    text=self.clean_atx_content(line.strip()),
                                                                    level=self.detect_atx_level(line))
                else:
                    # Remember line's content when checking the next line (if setex style header is detected then).
                    previous_line_content = line.strip()

                if header:
                    headers.append(header)

        # Write target file.
        output_file_name = os.path.basename(input_file)
        output_file = os.path.join(output_dir, output_file_name)

        with codecs.open(output_file, encoding='utf-8', mode='w') as output_file_handler:
            # Start the new file with the TOC header.
            output_file_handler.write('%s\n\n' % toc_header)

            # Add the TOC itself.
            previous_level = 1
            level_array = [0, 0, 0, 0, 0, 0]
            for text, current_level in headers:
                level_array[current_level - 1] += 1
                if current_level < previous_level:
                    for index in range(current_level, len(level_array)):
                        level_array[index] = 0

                output_file_handler.write('%s %d. [%s](#%s)\n' % ('\t' * (current_level - 1),
                                                                  level_array[current_level-1],
                                                                  text,
                                                                  self.generate_anchor(text)))

                # For next item.
                previous_level = current_level

            # Then add a horizontal rule.
            output_file_handler.write('\n---\n\n')

            # Finally add the rest of the content of the source file.
            with codecs.open(input_file, encoding='utf-8', mode='r') as source_file_handler:
                for line in source_file_handler:
                    output_file_handler.write(line)

    @staticmethod
    def get_header(kind, previous_line_content, text, level):
        if kind == 'setex':
            if previous_line_content == '':  # ignore horizontal rules (also matches the regex)
                return None, previous_line_content

        header = [text, level]
        previous_line_content = ''
        return header, previous_line_content

    @staticmethod
    def generate_anchor(text):
        # Convert spaces to hyphens and lowercase.
        anchor_text = text.lower().replace(' ', '-')

        # Remove every special character except hyphens, but kepp the usual unicode characters.
        return re.sub('([^\w\- üöäßéèêáàâóòô]|_)+', '', anchor_text)

    @staticmethod
    def detect_atx_level(line_content):
        for m, character in enumerate(line_content):
            if character == ' ':
                return m

    @staticmethod
    def clean_atx_content(line_content):
        clean_line = line_content

        for character in clean_line:
            if character == '#':
                clean_line = clean_line[1:]
            else:
                break

        for character in reversed(clean_line):
            if character == '#':
                clean_line = clean_line[:-1]
            else:
                break

        return clean_line.strip()
