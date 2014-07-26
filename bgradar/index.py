#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
from flask import render_template
from flask import request, Blueprint, g
from flask import current_app as app

index = Blueprint('index', __name__, template_folder='templates')


@index.route('/', methods=['GET'])
def index_page():
    return render_template('/index.html')
    # return 'index'