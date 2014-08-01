#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import urllib3


http = urllib3.PoolManager(10)
GOOGLE_GEOCODE_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
GOOGLE_API_KEY = ''


def get_address_by_lnglat(lng, lat):
    address = ''
    google_geocode_url = GOOGLE_GEOCODE_API_URL + "?sensor=true&latlng={0},{1}".format(lat, lng)

    google_geocode_url = google_geocode_url + '&language=zh-TW'

    resp = http.urlopen('GET', google_geocode_url)

    google_geocode = json.loads(resp.data)

    if 'results' not in google_geocode:
        return address

    if len(google_geocode['results']) == 0:
        return address

    address = google_geocode['results'][0].get('formatted_address', '')

    return address


if __name__ == '__main__':
    print get_address_by_lnglat(121.508272, 25.0421569)
