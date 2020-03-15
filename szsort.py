#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   szsort.py
@Time    :   2020/03/15 13:13:35
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
from random import randint
def listsort(list1):
    list1.sort()
mylist=[randint(-50,50) for _ in range(11)]
listsort(mylist)
print(mylist)