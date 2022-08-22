# coding=utf-8

import json
import os.path
import webullsdkcore

def _load_json_from_data_dir(name):
    entry_dir = os.path.dirname(os.path.abspath(webullsdkcore.__file__))
    json_file = os.path.join(entry_dir, "data", name)
    with open(json_file) as fp:
        return json.load(fp)