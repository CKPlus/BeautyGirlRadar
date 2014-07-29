BeautyGirlRadar
===============
Welcome to the BeautyGirlRadar wiki!

# API DOC

### Get hot point-

path:

    http://54.199.246.223:5000/api/bglbs?lng=121.508272&lat=25.0421569&dist=2

method:

    GET

response data:

    {
        "message": "OK",
        "results": [
            {
                "lat": 25.046,
                "count": 2,
                "lng": 121.518,
                "picurls": []
            },
            {
                "lat": 25.036,
                "count": 2,
                "lng": 121.5,
                "picurls": []
            },
            {
                "lat": 25.042,
                "count": 2,
                "lng": 121.508,
                "picurls": []
            }
        ]
    }

### Insert 正妹-

path:

    http://54.199.246.223:5000/api/bglbs

method:

    POST

request data:

    {
        "fbid": "123456",
        "lat":25.111,
        "lng":121.234
    }

response data:

    {
        "message": "OK",
        "results": [
        ]
    }

### upload pic-

path:

    http://54.199.246.223:5000/api/<uid>/upload

method:

    POST


response data:

    {
        "message": "OK",
        "results": ''
    }

### pic url-

    http://54.199.246.223:5000/static/uploads/765c80311b053a3e38e697a052ffa334.thumb


### beautygirl lbs function-

path:

    http://54.199.246.223:5000/api/bglbsdata/53d3b88ab6bb3b68040b4a90
    http://54.199.246.223:5000/api/bglbsdata

method:

    PATCH :  更新 comment fans_url
    GET   :  Get all , Get single

request data:

    {
        "comment": "大正妹"
        "fans_url" "更多美圖"
    }

response data:

    {
        "message": "OK",
        "results": [
            {
                "comment": "",
                "uid": "53d3b88ab6bb3b68040b4a90",
                "fans_url": "",
                "picurl": "4cdda716bb8b09684d8ae2239ce4a217",
                "lat": 25.111,
                "lng": 121.234
            }
        ]
    }
