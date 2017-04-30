# coding=utf-8
import unittest
import os
import requests

class baiduTest(unittest.TestCase):
    def setUp(self):
        self.headers = {}
    def test_baidu_normal0(self):
        url = 'https://www.baidu.com'
        r = requests.get(url,params={'': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
    def test_baidu_fault0(self):
        url = 'https://www.baidu.com'
        r = requests.get(url,params={'': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
