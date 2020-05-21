#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   decorator4.py
@Time    :   2020/05/21 21:12:59
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import math
def outer_none(func):
    def inner(*args,**kw):
        print('当前执行无参无返回值函数')
        func()
    return inner
def outer_re(func):
    def inner(*args,**kw):
        print('当前执行有返回值函数')
        res=func()
        return res
    return inner
def outer_rex(func):
    def inner(*args,**kw):
        print('当前执行有返回值有参数函数')
        res=func(*args,**kw)
        return res
    return inner
@outer_none
def sushu_none():
    for i in range(2,20000):
        flag=1
        for j in range(2,int(math.sqrt(i))):
            if i%j==0:
                flag=0
                break
        if(flag==1):
            print(i,end=' ')
    print('\n')
@outer_re
def sushu_re():
    count=0
    for i in range(2,10000):
        flag=1
        for j in range(2,int(math.sqrt(i))):
            if i%j==0:
                flag=0
                break
        if flag==1:
            count=count+1
    return count
@outer_rex
def sushu_rex(M):
    count=0
    for i in range(2,int(M)):
        flag=1
        for j in range(2,int(math.sqrt(i))):
            if i%j==0:
                flag=0
                break
        if flag==1:
            count=count+1
    return count
def main():
    sushu_none()
    print('素数有%d个'%sushu_re())
    print('素数有%d个'%sushu_rex(100))
if __name__ == "__main__":
    main()

        

