#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime

dbname_bgradar = 'bg_radar'
c_name_user = 'user'


class UserManager():

    def __init__(self, get_collection):
        self.__get_collection = get_collection

    def update_user(self, fbid):

        collection = self.__get_collection(dbname_bgradar, c_name_user)
        collection.update(
            {'fbid': fbid},
            {
                '$set': {
                    'utime': datetime.utcnow()
                },
                '$setOnInsert': {'ctime': datetime.utcnow()}
            }, upsert=True)
