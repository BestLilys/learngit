#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   ospric.py
@Time    :   2020/05/19 22:30:56
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os,datetime
def report(path):
    print('%-25s%-20s%-5s%-5s'%('名称','修改日期','类型','大小'))
    for file in os.listdir(path):
        filepath=os.path.join(path,file)
        date=os.path.getmtime(filepath)
        date=datetime.datetime.fromtimestamp(date).replace(microsecond=0)
        if os.path.isdir(filepath):
            sort='文件夹'
            size=''
        else:
            sort='文件'
            size=os.path.getsize(filepath)
        print('%-27s%-24s%-5s%-7s'%(file,date,sort,size))
path=input('请输入目标文件夹路径:')
report(path)