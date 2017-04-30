# coding=utf-8

import requests

URL_get = 'http://httpbin.org/ip'
r = requests.get(URL_get)
print r.text

URL_post = 'http://httpbin.org/post'
data = {'key1':'v1',
        'key2':'v2'
        }

r = requests.post(URL_post,data=data)
print r.text
print 'the heads info is:',r.headers
print 'the post status is :', r.status_code




