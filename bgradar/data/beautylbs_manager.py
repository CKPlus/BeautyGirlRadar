#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
from pymongo import GEO2D

dbname_bgradar = 'bg_radar'
c_name_beautylbs = 'beauty_lbs'


class BeautyLBSManager():
    def __init__(self, get_collection):
        self.__get_collection = get_collection
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        collection.ensure_index([('locs', GEO2D)])

    def update_lbs(self, fbid, lng, lat, pic_url):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        collection.insert({
            'fbid': fbid,
            'locs': [lng, lat],
            'picurl': pic_url,
            'ctime': datetime.utcnow()
            })

    def find_near(self, lng, lat):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        return collection.find({'locs': {'$near': [lng, lat]}})

    def find_near_by_distance(self, lng, lat, distance):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        return collection.find({
            'locs': {
                '$near': [100, 100],
                # '$maxDistance': distance/111.12
                '$maxDistance': 10
            }})
