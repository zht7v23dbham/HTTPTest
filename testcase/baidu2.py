# coding=utf-8
import unittest
import os
import requests

class baidu2Test(unittest.TestCase):
    def setUp(self):
        self.headers = {}
    def test_baidu2_fault1(self):
        url = 'https://www.baidu.com'
        r = requests.post(url,data={'': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
    def test_baidu2_fault0(self):
        url = 'https://www.baidu.com'
        r = requests.post(url,data={'': ''})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('' in r.text)
