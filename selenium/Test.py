# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import HTMLTestRunner
import sys
import os
from time import sleep

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        chromedriver = "C:\HTTPTest\HTTPTest\Drivers\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver =  webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_search_in_python_org(self):

        sleep(2)
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("Selenium2")
        self.driver.find_element_by_id("su").click()
        sleep(2)
    def tearDown(self):

        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
