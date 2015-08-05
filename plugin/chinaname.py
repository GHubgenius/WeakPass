#!/usr/bin/env python
#coding:utf-8

from plugin.doFile import readFile_func
from plugin.doFile import writeFile_func

#中文姓名组合
def chinaname_base(chinanameList):

    nameList = []                                       #根据中文姓名，生成缩写等

    nameLength = len(chinanameList)
    tmpName = ''
    for i in range(nameLength):                             #全拼 wangshaoda
        tmpName += chinanameList[i]
    nameList.append(tmpName)

    tmpName = chinanameList[0].capitalize()                 #首字母大写Wang
    tmpName1,tmpName2,tmpName3 = '','',''
    for i in range(1,nameLength):
        tmpName1 += chinanameList[i]                        #Wangshaoda
        tmpName2 += chinanameList[i][0]                     #Wangsd
        tmpName3 += chinanameList[i][0].capitalize()        #WangSD

    nameList.append(tmpName+tmpName1)
    nameList.append(tmpName+tmpName2)
    nameList.append(tmpName+tmpName3)

    tmpName = chinanameList[0][0].capitalize()              #首字母大写W
    tmpName1,tmpName2,tmpName3 = '','',''
    for i in range(1,nameLength):
        tmpName1 += chinanameList[i]                        #Wshaoda
        tmpName2 += chinanameList[i][0]                     #Wsd
        tmpName3 += chinanameList[i][0].capitalize()        #WSD

    nameList.append(tmpName+tmpName1)
    nameList.append(tmpName+tmpName2)
    nameList.append(tmpName+tmpName3)

    tmpName = ''                                            #小写wsd
    for i in range(nameLength):
        tmpName += chinanameList[i][0]
    nameList.append(tmpName)

    nameList.append(chinanameList[0])                       #姓 wang

    nameList.append(chinanameList[0].capitalize())          #姓大写 Wang

    return nameList

def chinaname_func(chinanameList):
    dicList = []                                        #最终的字典
    fileList = readFile_func('./dic/common.txt')       #读取common.txt的字典
    nameList = chinaname_base(chinanameList)
    for i in nameList:
        for j in fileList:
            dicList.append(i+j)
    writeFile_func(dicList)


#中文姓名和生日组合
def chinaname_birth_func(chinanameList):
    dicList = []
    nameList = chinaname_base(chinanameList)
    yList = readFile_func('./dic/y.txt')
    mList = readFile_func('./dic/m.txt')
    dList = readFile_func('./dic/d.txt')

    for i in nameList:
        for j in yList:
            for k in mList:
                for l in dList:
                    dicList.append(i+j+k+l)
    writeFile_func(dicList)


#中文姓名和公司组合
def chinaname_domain_func(chinanameList,domainList):
    dicList = []
    nameList = chinaname_base(chinanameList)

    for i in nameList:
        for j in domainList:
            dicList.append(i+j)
            dicList.append(i+'@'+j)
            dicList.append(i+'_'+j)
    writeFile_func(dicList)