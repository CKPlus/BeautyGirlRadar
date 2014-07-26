#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime
from pymongo import GEO2D

dbname_bgradar = 'bg_radar'
c_name_beautylbs = 'beauty_lbs'


class BeautyLBSManager():
    def __init__(self, get_collection):
        self.__get_collection = get_collection
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        collection.ensure_index([('locs', GEO2D)])

    def update_picurl(self, uid, pic_url):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        collection.update(
            {'_id': ObjectId(uid)},
            {
                '$set': {
                    'picurl': pic_url,
                    'utime': datetime.utcnow()
                }
            })

    def update_comment_fans(self, uid, comment, fans_url):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        collection.update(
            {'_id': ObjectId(uid)},
            {
                '$set': {
                    'comment': comment,
                    'fans_url': fans_url,
                    'utime': datetime.utcnow()
                }
            })

    def update_lbs(self, fbid, lng, lat, comment=None, fans_url=None, picurl=None):

        if picurl is None:
            picurl = ''

        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)

        if comment is None:
            comment = ''

        if fans_url is None:
            fans_url = ''

        id = ObjectId()

        collection.insert({
            '_id': id,
            'fbid': fbid,
            'locs': [lng, lat],
            'lng': lng,
            'lat': lat,
            'picurl': picurl,
            'comment': comment,
            'fans_url': fans_url,
            'ctime': datetime.utcnow()
            })

        return str(id)

    def find_all(self):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        return collection.find({})

    def find_by_fbid(self, obj_id):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        return collection.find_one({'_id': ObjectId(obj_id)})

    def find_near(self, lng, lat):
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        return collection.find({'locs': {'$near': [lng, lat]}})

    def find_hot_points(self, lng, lat, distance):
        """ retrun data format

        """
        collection = self.__get_collection(dbname_bgradar, c_name_beautylbs)
        distance = distance / 111.12
        max_lng = lng + distance
        min_lng = lng - distance
        max_lat = lat + distance
        min_lat = lat - distance

        lbs_cursor = collection.find(
            {
                'lng': {'$lte': max_lng, '$gte': min_lng},
                'lat': {'$lte': max_lat, '$gte': min_lat}
            })

        hot_points = {}

        for lbs_data in lbs_cursor:
            lng_tmp = float('%.3f' % lbs_data['lng'])
            lat_tmp = float('%.3f' % lbs_data['lat'])

            hot_point = (lng_tmp, lat_tmp)

            if hot_point not in hot_points:
                hot_profile = {}
                hot_profile['count'] = 1

                if len(lbs_data['picurl']) > 0:
                    hot_profile['picurls'] = [lbs_data['picurl']]
                else:
                    hot_profile['picurls'] = []

                hot_points[hot_point] = hot_profile

            else:
                hot_profile = hot_points[hot_point]
                new_count = hot_profile['count'] + 1
                new_picurls = hot_profile['picurls']

                if len(lbs_data['picurl']) > 0:
                    new_picurls.append(lbs_data['picurl'])

                hot_profile['count'] = new_count
                hot_profile['picurls'] = new_picurls
                hot_points[hot_point] = hot_profile

        return hot_points

        # return collection.find({'locs': {'$near': [50, 50], '$maxDistance': 1/111.12}})
        # return collection.find({
        #     'locs': {
        #         '$near': [lng, lat],
        #         # '$maxDistance': distance/111.12
        #         # '$maxDistance': 10
        #         '$maxDistance': 2/111.12
        #     }})