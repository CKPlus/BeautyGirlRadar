#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Blueprint

blueprint_bgradar = Blueprint(
    'bgradar',
    __name__,
    template_folder='templates')


SITE_NAME = "正咩走著瞧"

import views