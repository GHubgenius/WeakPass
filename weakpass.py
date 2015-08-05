#!/usr/bin/env python
#coding:utf-8
#author:0xExploit
#weibo:


import argparse
import common
from plugin.chinaname import chinaname_func
from plugin.chinaname import chinaname_domain_func
from plugin.chinaname import chinaname_birth_func
from plugin.domain import domain_func
from plugin.username import username_birth_func
from plugin.username import username_domain_func
from plugin.username import username_func



#解析命令行参数
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',dest='chinaname',type=str,help="input china username with ',',like 'wang,shao,shao' ")
    parser.add_argument('-d',dest='domain',type=str,help="input company name,like 'tencent,qq' ")
    parser.add_argument('-u',dest='username',type=str,help="input username,like 'admin' ")
    parser.add_argument('-n',dest='number',type=str,help="birth,custom")
    args = parser.parse_args()
    return args

def main():
    args = arg_parse()

    chinaname = args.chinaname
    domain = args.domain
    username = args.username
    number = args.number

    if(chinaname != None and chinaname != ''):
        chinanameList = common.splitCommma_func(chinaname)

        if(domain != None and domain != ''):
            domainList = common.splitCommma_func(domain)
            chinaname_domain_func(chinanameList,domainList)      #中文姓名和公司组合,包含中文姓名组合
        elif(number == 'birth'):
            chinaname_birth_func(chinanameList)                  #中文姓名和生日组合,包含中文姓名组合
        else:
            chinaname_func(chinanameList)                        #中文姓名组合

    elif(domain != None and domain != '' and username == None):
        domainList = common.splitCommma_func(domain)
        domain_func(domainList)                                  #公司组合

    elif(username != None and username != ''):
        usernameList = common.splitCommma_func(username)
        if(domain != None and domain != ''):
            domainList = common.splitCommma_func(domain)
            username_domain_func(usernameList,domainList)        #用户名和公司组合,包含用户名组合
        elif(number == 'birth'):
            username_birth_func(usernameList)                    #用户名和生日组合,包含用户名组合
        else:
            username_func(usernameList)                          #用户名组合
    else:
        pass


if __name__ == "__main__":
    main()

