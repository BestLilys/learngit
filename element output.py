#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   元素输出查找.py
@Time    :   2020/03/05 14:01:46
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here

import math
print("奇数:",end=' ')
for i in range(50):
    if (i%2!=0):
        print(i,end=' ')
print("\n偶数:",end=' ')
for i in range(50):
    if (i%2==0):
        print(i,end=' ')
print("\n质数:",end=' ')
for i in range(2,50):
    for j in range(2,((int)(math.sqrt(i))+1)):
        if(i%j==0):
            break
    else:
        print(i,end=' ')
print("\n能被23同时整除的数:",end=' ')
for i in range(50):
    if(i%6==0):
        print(i,end=' ')
