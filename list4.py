#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   list4.py
@Time    :   2020/05/18 14:10:55
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import time
from collections import deque
def listtime():
    begintime=time.perf_counter()
    mylist1=[]
    mylist2=[]
    for i in range(10):
        mylist1.insert(0,i)
        mylist2.append(i)
    endtime=time.perf_counter()
    return (endtime-begintime)
def dequetime():
    begintime=time.perf_counter()
    mylist1=deque()
    mylist2=deque()
    for i in range(10):
        mylist1.appendleft(i)
        mylist2.append(i)
    endtime=time.perf_counter()
    return (endtime-begintime)
print('列表时间:{}  deque时间:{}'.format(listtime(),dequetime()))