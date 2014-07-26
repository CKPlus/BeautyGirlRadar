#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
import json
from flask import Flask, render_template
from bgradar.api.data import close_error_connection
from bgradar.api.data import user_manager
from bgradar.api.data import beautylbs_manager

UPLOAD_FOLDER = 'bgradar/static/uploads/'


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app

app = create_app()

from bgradar.api.user import user
app.register_blueprint(user, url_prefix='/api')

from bgradar.api.beauty_lbs import beauty_lbs
app.register_blueprint(beauty_lbs, url_prefix='/api')

from bgradar.api.upload import upload
app.register_blueprint(upload, url_prefix='/api')

from bgradar.bgradar_app import blueprint_bgradar
app.register_blueprint(blueprint_bgradar, url_prefix='/bgradar')


# @app.errorhandler(Exception)
# def handle_error(error):
#     # close_error_connection()
#     return json.dumps({"error": str(error.message)}), 500


@app.route('/bgradarapi/test')
def test():
    user_manager.update_user('fbid')
    beautylbs_manager.update_lbs('fbid', 121.517542, 25.046084, 'pic_url')
    beautylbs_manager.update_lbs('fbid', 121.508272, 25.042157, 'pic_url')
    beautylbs_manager.update_lbs('fbid', 121.499945, 25.035877, 'pic_url')

    # beautylbs_manager.update_lbs('fbid', 25.046084, 121.517542, 'pic_url')
    # beautylbs_manager.update_lbs('fbid', 25.042157, 121.508272, 'pic_url')
    # beautylbs_manager.update_lbs('fbid', 25.035877, 121.499945, 'pic_url')
    # beautylbs_manager.update_lbs('fbid', 25.041535, 121.516029, 'pic_url')
    # beautylbs_manager.update_lbs('fbid', 25.063015, 121.551955, 'pic_url')
    # beautylbs_manager.update_lbs('fbid', 25.070401, 121.49668, 'pic_url')
    # near_data = beautylbs_manager.find_near(121.49, 25.03)
    # for bg_near in near_data:
    #     print bg_near

    # near_data = beautylbs_manager.find_near_by_distance(121.49, 25.03, 2)
    near_data = beautylbs_manager.find_near_by_distance(25.046084, 121.517542, 2)

    for bg_near in near_data:
        print bg_near
    return 'wellcome_page'