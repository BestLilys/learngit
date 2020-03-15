#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   mostelement.py
@Time    :   2020/03/15 12:52:28
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
from collections import Counter
def mostelement(string):
    mydict=Counter(string)
    countlist=list(mydict.items())
    countlist.sort(key=lambda x:x[1],reverse=True)
    print("{}:{}".format(countlist[0][0],countlist[0][1]))
string=input("请输入字符串值:")
mostelement(string)

    