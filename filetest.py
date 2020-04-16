#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   filetest.py
@Time    :   2020/04/16 22:26:31
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os
def createfile(filename):
    with open(filename,'a+') as f:
        f.write('How many roads must a man walk down\n')
        f.write('Before they call him a man\n')
        f.write('How many seas must a white dove sail\n')
        f.write('Before she sleeps in the sand\n')
        f.write('How many times must the cannon balls fly\n')
        f.write("Before they're forever banned\n")
        f.write('The answer, my friend, is blowing in the wind\n')
        f.write('The answer is blowing in the wind\n')
def insertinfo(filename,songname,singername,text):
    with open(filename,'r+') as f:
        mylist=[]
        for line in f.readlines():
            mylist.append(line)
        mylist.insert(0,songname+'--'+singername+'\n')
        mylist.append(text)
        f.seek(0)
        f.writelines(mylist)
def printtxt(filename):
    with open(filename,'r') as f:
        for line in f.readlines():
                print(line.strip())
createfile('Blowing in the wind.txt')
insertinfo('Blowing in the wind.txt',"Blowin' in the wind",'Bob Dylan','1962 by Warner Bros.Inc.')
printtxt('Blowing in the wind.txt')