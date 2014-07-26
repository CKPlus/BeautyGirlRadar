#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
from bgradar.app import blueprint_bgradar


@blueprint_bgradar.route('/', methods=['GET'])
def index_page():
    return render_template('/index.html')