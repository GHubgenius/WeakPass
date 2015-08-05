#!/usr/bin/env python
#coding:utf-8

from os import linesep

#将列表内容写入到文件中
def writeFile_func(dicList):
    filepath = './dic.txt'

    f = open(filepath,'a+')
    for i in dicList:
        f.writelines(i+linesep)
    f.close()

#读取文件内容
def readFile_func(filepath):
    fileList = []
    f1 = open(filepath)
    for i in f1:
        fileList.append(i.strip('\n').strip('\r'))
    return fileList