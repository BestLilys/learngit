#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   changeex.py
@Time    :   2020/04/16 22:07:40
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
filelist=os.listdir('img')
os.chdir(os.path.abspath('img'))
for filename in filelist:
    filesplist=os.path.splitext(filename)
    if(filesplist[1]=='.png'):
        newname=filesplist[0]+'.jpg'
        os.rename(filename,newname)