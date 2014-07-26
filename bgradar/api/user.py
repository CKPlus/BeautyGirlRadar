#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
from flask import request, Blueprint
from bgradar.api.data import user_manager


user = Blueprint('user', __name__)


@user.route('/user', methods=['POST', 'GET'])
def user_profile():
    if request.method == 'POST':
        req_body = json.loads(request.data)
        fbid = req_body['fbid']
        user_manager.update_user('fbid2')
        pass

    elif request.method == 'GET':
        pass

    return 'user'
