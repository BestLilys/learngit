#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   write&sort.py
@Time    :   2020/04/16 21:11:51
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
mylist=[]
with open("test.txt","r",encoding='utf-8') as f:
    for line in f.readlines():
        mylist.append(line.split())
mylist=mylist[1:]
for ele in mylist:
    ele[2]=int(ele[2])
mylist.sort(key=lambda x:x[2])
for ele in mylist:
    print(ele)   