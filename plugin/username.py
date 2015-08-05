#!/usr/bin/env python
#coding:utf-8

from plugin.doFile import readFile_func
from plugin.doFile import writeFile_func


#用户名组合
def username_func(usernameList):
    dicList = []
    fileList = readFile_func('./dic/common.txt')       #读取common.txt的字典

    for i in usernameList:
        for j in fileList:
            dicList.append(i+j)

    writeFile_func(dicList)


#用户名和生日组合
def username_birth_func(usernameList):
    dicList = []
    yList = readFile_func('./dic/y.txt')
    mList = readFile_func('./dic/m.txt')
    dList = readFile_func('./dic/d.txt')

    for i in usernameList:
        for j in yList:
            for k in mList:
                for l in dList:
                    dicList.append(i+j+k+l)
    writeFile_func(dicList)


#用户名和公司组合
def username_domain_func(usernameList,domainList):
    dicList = []

    for i in usernameList:
        for j in domainList:
            dicList.append(i+j)
            dicList.append(i+'@'+j)
            dicList.append(i+'_'+j)
    writeFile_func(dicList)