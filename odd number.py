#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   odd number.py
@Time    :   2020/03/09 19:52:50
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import random
def oddnum(mylist):
    for i in mylist:
        if(i%2!=0):
            print(i,end=' ')
mylist=[random.randint(-10,10) for _ in range(10)]
oddnum(mylist)