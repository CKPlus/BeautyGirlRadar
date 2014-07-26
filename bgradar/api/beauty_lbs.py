#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from datetime import datetime
from hashlib import md5
import json
from PIL import Image
from werkzeug.utils import secure_filename
from flask import request, Blueprint, jsonify
from flask import current_app as app
from bgradar.api.data import beautylbs_manager
from bgradar.api.packet import ClientResults, ClientResult


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

        pass

    return clientresults.to_json(), status_code

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# @beauty_lbs.route('/upload/<fbid>', methods=['POST'])
# def upload(fbid):
#     status_code = 200
#     print "test"

#     path = str(os.path.join('upload_folder', 'test'))
#     clientresult = ClientResult()

#     file = request.files['file']
#     print file.filename

#     if file:
#         print "allowed fbid = " + fbid
#         str_datetime = datetime.datetime.now(tzlocal()).strftime("%s.000")
#         filename = secure_filename(file.filename)
#         m = md5.new()
#         m.update(filename)
#         m.update(str_datetime)
#         photo_id = binascii.hexlify(m.digest())

#         path = str(os.path.join(upload_folder, photo_id))
#         file.save(path)

#         im = Image.open(path)
#         im = im.convert('RGB')
#         im.thumbnail((300, 300), Image.ANTIALIAS)
#         im.save(path + ".thumb", 'PNG')

#         beautylbs_manager.update_picurl(fbid, photo_id)

#         return clientresult, status_code

#     return jsonify(**{"Error": "Input Error"})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@beauty_lbs.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
