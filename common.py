#!/usr/bin/env python
#coding:utf-8

#用逗号分隔，返回列表
def splitCommma_func(string):
    if ',' in string:
        result = string.split(',')
    else:
        result = []
        result.append(string)
    return result

