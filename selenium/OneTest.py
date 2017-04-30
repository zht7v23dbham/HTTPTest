# -*- coding: utf-8 -*-
import unittest
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # firefox 实际安装路径
        ffdriver = "C:\\Program Files (x86)\\\Mozilla Firefox\\firefox.exe"

        os.environ["webdriver.firefox.driver"] = ffdriver

        self.driver = webdriver.Firefox(ffdriver)

    def test_search_in_python_org(self):
        driver = self.driver

        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("Selenium2")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()