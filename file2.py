#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   file2.py
@Time    :   2020/03/30 19:03:12
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
with open('input.txt','r') as f:
    string=f.read()
    linelist=['零','一','二','三','四','五','六','七','八','九','十']
    mylist=string.split('\n')
    n=0
    for i in mylist:
        n=n+1
        print('{}:#第{}行:{}'.format(n,linelist[n],i))