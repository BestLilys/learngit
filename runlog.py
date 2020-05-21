#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   runlog.py
@Time    :   2020/05/21 20:18:15
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import time
def outer(func):
    def inner(*args,**kw):
        path=r'C:\Users\24297\Desktop\log.txt'
        with open(path,'a',encoding='utf-8')as f:
            f.write('在{}调用了{}函数\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__))
        func(*args,**kw)
    return inner