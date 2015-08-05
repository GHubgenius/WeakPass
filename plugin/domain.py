#!/usr/bin/env python
#coding:utf-8

from plugin.doFile import readFile_func
from plugin.doFile import writeFile_func

#公司组合
def domain_func(domainList):
    dicList = []
    fileList = readFile_func('./dic/common.txt')       #读取common.txt的字典

    for i in domainList:
        for j in fileList:
            dicList.append(i+j)

    writeFile_func(dicList)