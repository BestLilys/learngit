#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   accountsafe.py
@Time    :   2020/05/18 16:05:26
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import hashlib
def saveinfo():
    accountlist=[]
    for i in range(5):
        md5=hashlib.md5()
        name,account,password=input('请输入姓名账号密码(空格分隔):').split()
        md5.update(password.encode('utf-8'))
        accountlist.append((name,account,md5.hexdigest()))
    with open('accountlist.txt','w')as f:
        for i in range(5):
            f.write('{} {} {}\n'.format(accountlist[i][0],accountlist[i][1],accountlist[i][2]))
saveinfo()

