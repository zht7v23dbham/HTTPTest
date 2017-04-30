# coding=utf-8

import unittest
import os
import imp



path = os.getcwd() + '\\testcase'
fileList = os.listdir(path)


moduleList = [x.split('.')[0] for x in fileList]
moduleList = list(set(moduleList))
moduleList.remove('__init__')

mObj = []
for mName in moduleList:
    mObj.append(imp.load_source(mName,os.getcwd()+'\\testcase\\'+mName+'.py'))

testSuite = unittest.TestSuite()
loader = unittest.defaultTestLoader
for m in mObj:
    tests = loader.loadTestsFromModule(m)
    testSuite.addTests(tests)

unittest.TextTestRunner().run(testSuite)


