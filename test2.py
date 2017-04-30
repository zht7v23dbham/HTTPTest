# coding=utf-8

import os

paramDict = {'getip': {'faultParams': [{'': ''}], 'normalResult': 'str1,str2', 'interfaceType': 'get', 'normalState': '200.0', 'url': 'http://httpbin.org/ip', 'faultResult': 'str', 'faultState': '200.0', 'normalParams': [{'': ''}]},\
             'postIntf': {'faultParams': [{'key2': 'v34', 'key1': 'v34'}], 'normalResult': 'v11', \
            'interfaceType': 'post', 'normalState': '200.0', 'url': 'http://httpbin.org/post', 'faultResult': 'str', 'faultState': '200.0', 'normalParams': [{'key2': 'v2', 'key1': 'v1'}, {'key2': 'v2', 'key1': 'v11'}, \
            {'key2': 'v2', 'key1': 'v111'}, {'key2': 'v22', 'key1': 'v1'}, {'key2': 'v222', 'key1': 'v1'}]}}



def makeTestcase(dictData):
    keys = dictData.keys()
    for key in keys:
        filePath = os.getcwd() + '\\testcase\\' + key + '.py'
        fh = open(filePath, 'w')
        fh.write('# coding=utf-8\n'
                 'import unittest\n'
                 'import os\n'
                 'import requests\n'
                 '\n'
                 'class ' + key + 'Test' + '(unittest.TestCase):\n'
                 )
        #遍历正常的列表
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
            else:
                continue
            i+=1

        # 遍历异常的列表
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
            else:
                continue
            j += 1

        fh.close()

if __name__ == '__main__':
    makeTestcase(paramDict)


