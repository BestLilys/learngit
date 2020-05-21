#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   runtime.py
@Time    :   2020/05/21 18:01:13
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import time,random
def outer(function):
    def inner(*args,**kw):
        begintime=time.perf_counter()
        function(*args,**kw)
        endtime=time.perf_counter()
        print('运行时间:{}'.format(endtime-begintime))
    return inner