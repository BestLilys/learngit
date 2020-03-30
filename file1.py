#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   file1.py
@Time    :   2020/03/30 18:35:53
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
mylist=[]
while(True):
    string=input()
    mylist.append(string)
    if(string==''):
        break
print(mylist)
with open('test.txt','w') as f:
        for i in mylist:
            f.write(i+'\n')