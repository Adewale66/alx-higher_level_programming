#!/usr/bin/python3

"""Json module"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    import json
    return json.dumps(my_obj)
