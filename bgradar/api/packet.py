#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
import json
from datetime import datetime


class ClientResults(object):

    def __init__(self):
        self.message = 'OK'
        self.results = []

    def to_json(self):
        return json.dumps(self, default=to_json)


class ClientResult(object):

    def __init__(self):
        self.message = 'OK'
        self.result = {}

    def to_json(self):
        return json.dumps(self, default=to_json)


def to_json(python_object):
    if isinstance(python_object, ClientResult):
        return {
            'message': python_object.message,
            'result': python_object.result,
        }

    if isinstance(python_object, ClientResults):
        return {
            'message': python_object.message,
            'results': python_object.results,
        }

    if isinstance(python_object, datetime):
        if python_object:
            return "{0} {1}".format(python_object.strftime("%Y-%m-%d"),
                                    python_object.strftime("%H:%M:%S"))
        else:
            return None
