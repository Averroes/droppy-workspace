#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
import json
import os
import requests
import sys
from base64 import b64encode

sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, 'DropPy.Common')))
from file_tools import get_file_paths_from_directory


class Task(object):
    """
    Documentation: https://docs.droppyapp.com/tasks/web-imgur-upload
    """
    def __init__(self, input_paths, output_dir, **kwargs):
        # Get keyword arguments.
        client_id = kwargs.get(str('client_id'), '')

        # Check for required arguments.
        if len(client_id) == 0:
            sys.exit('No Imgur client_id passed')

        # Process files and directories.
        for input_path in input_paths:
            if os.path.isfile(input_path):
                self.upload_file(input_path, output_dir, client_id)

            elif os.path.isdir(input_path):
                output_sub_dir = os.path.join(output_dir, os.path.basename(input_path))
                os.makedirs(output_sub_dir)

                contained_files = get_file_paths_from_directory(input_path)
                for contained_file in contained_files:
                    self.upload_file(contained_file, output_dir, client_id)

    @classmethod
    def upload_file(cls, input_file, output_dir, client_id):
        response = requests.post('https://api.imgur.com/3/image',
                                 headers={'authorization': 'Client-ID %s' % client_id},
                                 data={'image': b64encode(open(input_file, 'rb').read()),
                                       'type': 'base64'}
                                 )

        json_response = json.loads(response.text)

        if 'status' in json_response:
            if json_response['status'] == 200:
                if 'data' in json_response:
                    if 'link' in json_response['data']:
                        cls.create_webloc_file(json_response['data']['link'], input_file, output_dir)
                    else:
                        sys.exit('Upload successful but link not found in server response (%s)' % json_response)
                else:
                    sys.exit('Upload successful but data not found in server response (%s)' % json_response)
            else:
                sys.exit('Upload not successful (%s)' % json_response)
        else:
            sys.exit('Upload not successful (%s)' % json_response)

    @staticmethod
    def create_webloc_file(url, input_file, output_dir):
        output_file_name, _ = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(output_dir, output_file_name + '.webloc')

        with codecs.open(output_file, encoding='utf-8', mode='w') as output_file_handler:
            output_file_handler.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            output_file_handler.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"')
            output_file_handler.write(' "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
            output_file_handler.write('<plist version="1.0">\n')
            output_file_handler.write('  <dict>\n')
            output_file_handler.write('    <key>URL</key>\n')
            output_file_handler.write('    <string>%s</string>\n' % url)
            output_file_handler.write('  </dict>\n')
            output_file_handler.write('</plist>\n')
