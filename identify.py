#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   identify.py
@Time    :   2020/05/21 20:37:53
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import hashlib
def outer(func):
    def inner(*args,**kw):
        accountdict={}
        with open('accountlist.txt','r') as f:
            for i in range(5):
                account,password=(f.readline().split())
                accountdict[account]=password
        account=input('请输入账号:')
        if account in accountdict:
            password=input('请输入密码:')
            md5=hashlib.md5()
            md5.update(password.encode('utf-8'))
            if md5.hexdigest() in accountdict[account]:
                print('登录成功')
                func(*args,**kw)
            else:
                print('密码错误')
        else :
            print('账号错误')
    return inner