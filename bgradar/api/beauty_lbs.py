#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from datetime import datetime
from hashlib import md5
import json
from PIL import Image
from werkzeug.utils import secure_filename
from flask import request, Blueprint, jsonify, redirect, url_for
from flask import current_app as app
from bgradar.api.data import beautylbs_manager
from bgradar.api.packet import ClientResults, ClientResult
from bgradar.api.packet import ClientHotPoints


beauty_lbs = Blueprint('beauty_lbs', __name__)


@beauty_lbs.route('/bglbs', methods=['POST', 'GET'])
def user_profile():
    status_code = 200
    clientresults = ClientResults()

    if request.method == 'POST':
        req_body = json.loads(request.data)
        fbid = req_body['fbid']
        lat = req_body['lat']
        lng = req_body['lng']
        beautylbs_manager.update_lbs(fbid, lng, lat)

    elif request.method == 'GET':
        lng = float(request.args.get('lng', 0.0))
        lat = float(request.args.get('lat', 0.0))
        distance = float(request.args.get('dist', 2))

        # hot_points = beautylbs_manager.find_hot_points(121.234, 25.111, 2)
        hot_points = beautylbs_manager.find_hot_points(lng, lat, distance)

        for lnglat, hot_profile in hot_points.items():
            print lnglat, hot_profile
            client_hotpoints = ClientHotPoints()
            client_hotpoints.lng = lnglat[0]
            client_hotpoints.lat = lnglat[1]
            client_hotpoints.count = hot_profile['count']
            client_hotpoints.picurls = hot_profile['picurls']
            clientresults.results.append(client_hotpoints)

    return clientresults.to_json(), status_code
