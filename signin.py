#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   signin.py
@Time    :   2020/05/18 16:27:39
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import hashlib
def login():
    namelist=[]
    accountdict={}
    with open('accountlist.txt','r') as f:
        for i in range(5):
            name,account,password=(f.readline().split())
            namelist.append(name)
            accountdict[name]=(account,password)
    name=input('请输入姓名:')
    if name in namelist:
        account=input('请输入账号:')
        if account in accountdict[name]:
            password=input('请输入密码:')
            md5=hashlib.md5()
            md5.update(password.encode('utf-8'))
            if md5.hexdigest() in accountdict[name]:
                print('登录成功')
            else:
                print('密码错误')
        else :
            print('账号错误')
    else:
        print("没有此学生")
login()    
