# coding=utf-8
import unittest
import os
import requests

class getipTest(unittest.TestCase):
    def setUp(self):
        self.headers = {}
    def test_getip_normal0(self):
        url = 'http://httpbin.org/ip'
        r = requests.get(url,params={'': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
    def test_getip_fault0(self):
        url = 'http://httpbin.org/ip'
        r = requests.get(url,params={'': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
