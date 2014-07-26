#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask.ext import restful


class UserView(restful.Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {}