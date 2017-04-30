# coding=utf-8

# Author：zuohaitao

import xlrd
import os
import imp
import unittest

#依据excle中的接口信息，生成接口的字典数据
def genSourceData(file):
    #打开excle
    wBook = xlrd.open_workbook(file)
    sheetName = wBook.sheet_names()[0]
    sheet = wBook.sheet_by_name(sheetName)
    interfaceList = []

    #获取接口信息，如下的结构：[['getip', 1, 1], ['postIntf', 2, 2]]
    nrows = sheet.nrows
    for i in range(1, nrows):
        if sheet.cell(i, 0).value != '':
            interfaceName = str(sheet.cell(i,0).value)
            interfaceRow = i
            interfaceList.append([interfaceName, interfaceRow])
    lenList = []
    for i in range(len(interfaceList)-1):
        lenList.append(interfaceList[i+1][1]-interfaceList[i][1])
    lenList.append(nrows-interfaceList[len(interfaceList)-1][1])

    for i in range(len(interfaceList)):
        interfaceList[i].append(lenList[i])

    print interfaceList

    #获取消息体的内容列表
    def getParams(interfaceL, normalParams=True):
        pList = []
        resultList = []
        if normalParams == True:
            colNum = 4
        else:
            colNum = 5

        for j in range(interfaceL[1],interfaceL[1]+interfaceL[2]):
            keyName = str(sheet.cell(j,3).value)
            keyVarList = str(sheet.cell(j,colNum).value).split(',')

            pList.append([{keyName:x} for x in keyVarList])

        if pList == []:
            return pList

        aLen = len(pList)
        baseDict = {}
        resultList = []
        for i in range(aLen):
            baseDict = dict(baseDict.items() + pList[i][0].items())

        resultList.append(baseDict)
       # print baseDict
       # print resultList

        #替换每一个参数
        for i in range(0, len(pList)):
            for j in range(1, len(pList[i])):
                tmpDict = baseDict.copy()
                print 'tmpDict is ' + str(tmpDict)
                tmpDict.pop(pList[i][j].keys()[0])
                tmpDict = dict(tmpDict.items() + pList[i][j].items())
                resultList.append(tmpDict)
        return resultList

    #获取消息体中的key:value
    sourceDataDict = {}
    for i in range(len(interfaceList)):
        interfaceType = str(sheet.cell(interfaceList[i][1],1).value)
        url = str(sheet.cell(interfaceList[i][1],2).value)
        mormalResult = str(sheet.cell(interfaceList[i][1],6).value)
        faultResult = str(sheet.cell(interfaceList[i][1],7).value)
        normalState = str(sheet.cell(interfaceList[i][1],8).value)
        faultState = str(sheet.cell(interfaceList[i][1],9).value)
        normalParams = getParams(interfaceList[i],True)
        faultParams = getParams(interfaceList[i],False)
        sourceDataDict[interfaceList[i][0]] = {'interfaceType':interfaceType,
                                               'url':url,
                                               'normalResult':mormalResult,
                                               'faultResult':faultResult,
                                               'normalState':normalState,
                                               'faultState':faultState,
                                               'normalParams':normalParams,
                                               'faultParams':faultParams
                                               }
    print  sourceDataDict
    return sourceDataDict

# 生成测试类  testcase
def makeTestcase(dictData):
    keys = dictData.keys()
    for key in keys:
        #针对没一个接口，生成一个文件，写文件头信息
        filePath = os.getcwd() + '\\testcase\\' + key + '.py'
        fh = open(filePath, 'w')
        fh.write('# coding=utf-8\n'
                 'import unittest\n'
                 'import os\n'
                 'import requests\n'
                 '\n'
                 'class ' + key + 'Test' + '(unittest.TestCase):\n'
                 )
        #执行案例前生成

        fh.write('    def setUp(self):\n'
                 "        #请求头信息\n"
                 '        self.headers = {}\n'
                 )


        #执行登录参数获取  token
        fh.write('    def GetToken(self):\n'
                 "        #登录参数获取  token\n"
                 "        url = 'https://api.bs.pre.gomeplus.com/v3/user/loginTokenGenerateForTestAction'\n"
                 "        r = requests.get(url,params="+str(param)+")\n\n"
                 "        self.assertTrue(r.status_code=="+str(int(dictData[key]['normalState'].split('.')[0]))+")\n"
                 "        self.assertTrue('"+str(dictData[key]['normalResult'])+"' in r.text)\n"
                 )


        #遍历正常的列表，生成正常测试用例
        i=0
        for param in dictData[key]['normalParams']:
            if dictData[key]['interfaceType'] == 'get':
                fh.write('    def test_'+key+'_normal'+str(i)+'(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.get(url,params="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['normalState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['normalResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'post':
                fh.write('    def test_' + key + '_normal' + str(i) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['normalState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['normalResult'])+"' in r.text)\n"
                         )
            elif dictData[key]['interfaceType'] == 'put':
                 fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'delete':
                 fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            else:
                continue
            i+=1

        # 遍历异常的列表，生成异常测试用例
        j = 0
        for param in dictData[key]['faultParams']:
            if dictData[key]['interfaceType'] == 'get':
                fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.get(url,params="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'post':
                fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'put':
                 fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            elif dictData[key]['interfaceType'] == 'delete':
                 fh.write('    def test_' + key + '_fault' + str(j) + '(self):\n'
                         "        url = '"+dictData[key]['url']+"'\n"
                         "        r = requests.post(url,data="+str(param)+")\n\n"
                         "        #assert here\n"
                         "        self.assertTrue(r.status_code=="+str(int(dictData[key]['faultState'].split('.')[0]))+")\n"
                         "        self.assertTrue('"+str(dictData[key]['faultResult'])+"' in r.text)\n"
                        )
            else:
                continue
            j += 1
        print param
        fh.close()

#执行测试用例
def executeTestcase():
    #获取所有的测试文件
    path = os.getcwd() + '\\testcase'
    fileList = os.listdir(path)

    moduleList = [x.split('.')[0] for x in fileList]
    moduleList = list(set(moduleList))
    if '__init__' in moduleList:
        moduleList.remove('__init__')

    #导入所有测试模块
    mObj = []
    for mName in moduleList:
        mObj.append(imp.load_source(mName, os.getcwd() + '\\testcase\\' + mName + '.py'))

    #将所有的测试模块加载到TestSuite中
    testSuite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    for m in mObj:
        tests = loader.loadTestsFromModule(m)
        testSuite.addTests(tests)
    #执行测试套中的用例
    unittest.TextTestRunner().run(testSuite)


if __name__ == "__main__":
    fileName = "C:\\Users\\zuohaitao\\Desktop\\接口测试框架汇总\\HTTPTest\\HTTPTest"
    dictData = genSourceData(fileName)
    makeTestcase(dictData)
    executeTestcase()










