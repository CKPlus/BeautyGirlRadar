#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
from flask import request, Blueprint
from bgradar.api.data import beautylbs_manager


beauty_lbs = Blueprint('beauty_lbs', __name__)


@beauty_lbs.route('/bglbs', methods=['POST', 'GET'])
def user_profile():
    if request.method == 'POST':
        req_body = json.loads(request.data)
        fbid = req_body['fbid']
        lat = req_body['lat']
        lng = req_body['lng']
        beautylbs_manager.update_lbs(fbid, lng, lat, 'pic_url')

    elif request.method == 'GET':
        pass

    return 'user'
