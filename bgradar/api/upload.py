#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from datetime import datetime
from hashlib import md5
import json
import binascii
from PIL import Image
from dateutil.tz import tzlocal
from werkzeug.utils import secure_filename
from flask import request, Blueprint, jsonify, redirect, url_for
from flask import current_app as app
from bgradar.api.data import beautylbs_manager
from bgradar.api.packet import ClientResult


upload = Blueprint('upload', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@upload.route('/<fbid>/upload', methods=['GET', 'POST'])
def upload_file(fbid):
    if request.method == 'POST':
        clientresult = ClientResult()
        file = request.files['file']
        if file and allowed_file(file.filename):

            str_datetime = datetime.now(tzlocal()).strftime("%s.000")
            filename = secure_filename(file.filename)
            m = md5()
            m.update(filename)
            m.update(str_datetime)
            photo_id = binascii.hexlify(m.digest())

            path = os.path.join(app.config['UPLOAD_FOLDER'], photo_id)
            file.save(path)

            im = Image.open(path)
            im = im.convert('RGB')
            im.thumbnail((300, 300), Image.ANTIALIAS)
            im.save(path + ".thumb", 'PNG')

            # return redirect(url_for('uploaded_file', filename=filename))
            beautylbs_manager.update_picurl(fbid, photo_id)
            return clientresult.to_json()

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
