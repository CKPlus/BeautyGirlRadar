#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
from flask import render_template

from . import blueprint_bgradar


@blueprint_bgradar.route('/', methods=['GET'])
def index_page():
    return render_template('/index.html')