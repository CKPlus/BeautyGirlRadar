#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json

from flask import request, Blueprint
from bgradar.api.data import beautylbs_manager
from bgradar.api.packet import ClientResults, ClientResult
from bgradar.api.packet import ClientHotPoints, ClientLBSData


beauty_lbs = Blueprint('beauty_lbs', __name__)


@beauty_lbs.route('/bglbs', methods=['POST', 'GET'])
def lbs_profile():
    status_code = 200
    clientresults = ClientResults()

    if request.method == 'POST':
        print 'data : {0}'.format(request.data)
        req_body = json.loads(request.data)
        fbid = req_body['fbid']
        lat = req_body['lat']
        lng = req_body['lng']
        uid = beautylbs_manager.update_lbs(fbid, lng, lat)
        resp_body = {"uid": uid}

        return json.dumps(resp_body), status_code

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


@beauty_lbs.route('/bglbsdata', methods=['GET'])
@beauty_lbs.route('/bglbsdata/<uid>', methods=['GET', 'PATCH'])
def get_all_lbs_profile(uid=None):
    status_code = 200
    clientresults = ClientResults()

    if uid:
        if request.method == 'GET':
            bglbs_data = beautylbs_manager.find_by_fbid(uid)
            if bglbs_data:
                client_lbs_data = ClientLBSData()
                client_lbs_data.uid = str(bglbs_data['_id'])
                client_lbs_data.lng = bglbs_data['lng']
                client_lbs_data.lat = bglbs_data['lat']
                client_lbs_data.comment = bglbs_data.get('comment', '')
                client_lbs_data.fans_url = bglbs_data.get('fans_url', '')
                client_lbs_data.picurl = bglbs_data.get('picurl', '')

                clientresults.results.append(client_lbs_data)
        else:
            req_body = json.loads(request.data)
            comment = req_body['comment']
            fans_url = req_body['fans_url']
            beautylbs_manager.update_comment_fans(uid, comment, fans_url)

        return clientresults.to_json(), status_code
    else:
        bglbs_cursor = beautylbs_manager.find_all()

        for bglbs_data in bglbs_cursor:
            client_lbs_data = ClientLBSData()
            client_lbs_data.uid = str(bglbs_data['_id'])
            client_lbs_data.lng = bglbs_data['lng']
            client_lbs_data.lat = bglbs_data['lat']
            client_lbs_data.comment = bglbs_data.get('comment', '')
            client_lbs_data.fans_url = bglbs_data.get('fans_url', '')
            client_lbs_data.picurl = bglbs_data.get('picurl', '')
            clientresults.results.append(client_lbs_data)
        return clientresults.to_json(), status_code


