#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   sum.py
@Time    :   2020/03/09 19:31:38
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
def sum(*inttuple):
    sum=0
    for n in inttuple:
        sum=sum+n
    print(sum)
    return sum