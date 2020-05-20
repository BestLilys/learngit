#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   sizesearch.py
@Time    :   2020/05/20 15:07:14
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
def sizeget(path):
    size=0
    for root,dirs,files in os.walk(path):
        for file in files:
            size=size+os.path.getsize(os.path.join(root,file))
    print (size)
path=input('请输入文件夹地址:')
sizeget(path)