# Creat by wangyang  2015-8-6

# -*- coding: utf-8 -*-
import json
from urllib import urlencode
import urllib2
from nose.tools import assert_equals
import sys
sys.path.append("../")
import get_response
import ConfigParser

# config = ConfigParser.ConfigParser()
# config.read('../conf/config.conf')
# playerId = config.get('global', 'playerId')
# url = config.get('global', 'url')
subjectId = '43'

def test_7(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1000,3],       #7 7 7 
                [3,1000,3],
                [3,1000,3]
            ],
            [
                [3,1000,3],       # 7 7 bar 
                [3,1000,3],
                [3,1,3]
            ],
            [
                [3,1000,3],       # 7 wild X
                [3,1,3],
                [3,1,3]
            ],
            [
                [3,1000,3],       # any 7
                [3,1001,3],
                [3,1002,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded

def test_bar(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1001,3],       #3bar
                [3,1001,3],
                [3,1001,3]
            ],
            [
                [3,1002,3],       #2bar
                [3,1002,3],
                [3,1002,3]
            ],
            [
                [3,1003,3],       #bar
                [3,1003,3],
                [3,1003,3]
            ],
            [
                [3,1001,3],       #any bar
                [3,1002,3],
                [3,1003,3]
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)      
        return ret_loaded

def test_wild(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1,3],
                [3,1,3],
                [3,1,3]   #wild wild 1x
            ],
            [
                [3,1,3],
                [3,1,3],
                [3,1,3]   #wild wild 2x
            ],
            [
                [3,1,3],
                [3,1,3],
                [3,1,3]   #wild wild 3x
            ],
            [
                [3,1,3],
                [3,1,3],
                [3,1,3]   #wild wild 7x
            ],
            [
                [3,1,3],
                [3,1,3],
                [3,1,3]   #wild wild 10x
            ],
            [
                [3,1,3],
                [3,1,3],
                [3,1,3]   #wild wild wild
            ],
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded

def test_7_wild(playerId,url):
        #global playerId
        #global url
        global subjectId
        data = {
        "playerId" : playerId,
        "subjectId":subjectId,
        "panels" : [
            [
                [3,1,3],       #wild 7 10x
                [3,1000,3],
                [3,1,3],
            ],
            [
                [3,1,3],       #wild 7 10x
                [3,1001,3],
                [3,1,3],
            ],
           [
                [3,1,3],       #wild 7 10x
                [3,1002,3],
                [3,1,3],
            ],
            [
                [3,1,3],       #wild 7 10x
                [3,1003,3],
                [3,1,3],
            ]
        ]
    }
        ret_loaded = get_response.Post_response(url,data)
        return ret_loaded
