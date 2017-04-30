# -*- coding: utf-8 -*-
#import unittest
from selenium import webdriver
import os
from time import sleep

if __name__ == '__main__':
    driver = webdriver.Ie()

    Iedriver = webdriver.Ie(executable_path="C:\HTTPTest\HTTPTest\Drivers\IEDriverServer.exe")
    # IeDriver = "C:\HTTPTest\HTTPTest\Drivers\IEDriverServer.exe"
    os.environ["webdriver.Ie.iedriver"] = Iedriver
    driver = webdriver.Chrome(Iedriver)
    sleep(10)
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("Selenium2")
    driver.find_element_by_id("su").click()
    sleep(10)
    driver.close()

