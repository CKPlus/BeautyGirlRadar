#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from bgradar.api.data.user_manager import UserManager
from bgradar.api.data.beautylbs_manager import BeautyLBSManager


# mongodb_connect_string = "mongodb://gogofun:gogofun@localhost:27017"
mongodb_connect_string = "mongodb://gogofun:gogofun@54.92.113.106:27017"

global_connection = None


def get_collection(dbname, collname):
    global global_connection

    while global_connection is None:
        try:
            global_connection = MongoClient(mongodb_connect_string, max_pool_size=500)

        except Exception as e:
            global_connection = None

    return global_connection[dbname][collname]


def close_error_connection():
    global global_connection
    if global_connection is not None:
        global_connection.close()
        global_connection = None

user_manager = UserManager(get_collection)
beautylbs_manager = BeautyLBSManager(get_collection)
