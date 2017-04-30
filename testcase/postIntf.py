# coding=utf-8
import unittest
import os
import requests

class postIntfTest(unittest.TestCase):
    def setUp(self):
        self.headers = {}
    def test_postIntf_normal0(self):
        url = 'http://httpbin.org/post'
        r = requests.post(url,data={'key1': 'v1'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('headers' in r.text)
    def test_postIntf_normal1(self):
        url = 'http://httpbin.org/post'
        r = requests.post(url,data={'key1': 'v11'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('headers' in r.text)
    def test_postIntf_normal2(self):
        url = 'http://httpbin.org/post'
        r = requests.post(url,data={'key1': 'v111'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('headers' in r.text)
    def test_postIntf_fault0(self):
        url = 'http://httpbin.org/post'
        r = requests.post(url,data={'key1': 'v34'})

        #assert here
        self.assertTrue(r.status_code==200)
        self.assertTrue('form' in r.text)
