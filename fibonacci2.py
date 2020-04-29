#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   fibonacci2.py
@Time    :   2020/03/15 12:16:27
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
def fibonacci(n):
    filist=[1,1]
    while filist[-1]<n:
        filist.append(filist[-1]+filist[-2])
    print(filist[0:-1])
n=int(input("请输入n大小:"))
fibonacci(n)