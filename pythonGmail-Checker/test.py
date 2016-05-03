#!/usr/bin/env python

import json
file_path = open('config.py', 'r')
json_file = file_path.read()
json_data = json.loads(json_file)
print json_data["credentials"][0]["username"]
