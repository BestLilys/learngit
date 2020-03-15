#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   scorejud.py
@Time    :   2020/03/15 12:44:45
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
from random import randint
scorelist=[randint(1,100) for _ in range(21)]
degreedict={}
for i in scorelist:
    if(i>=90):
        degreedict[i]='A'
    elif(i>=80 and i<90):
        degreedict[i]='B'
    elif(i>=80 and i<80):
        degreedict[i]='C'
    else:
        degreedict[i]='D'
    print("score:{}  degree:{}".format(i,degreedict[i]))