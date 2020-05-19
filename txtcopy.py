#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   txtcopy.py
@Time    :   2020/05/19 22:00:35
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
def copy(oldpath,newloc):
    info=''
    with open(oldpath,'r') as f1:
        info=f1.read()
    newpath=os.path.join(newloc,os.path.basename(oldpath))
    with open(newpath,'w') as f2:
        f2.write(info)
oldpath,newloc=input('请输入源文件路径和复制地址(空格隔开):').split()
copy(oldpath,newloc)

