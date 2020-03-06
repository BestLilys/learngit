# -*- encoding: utf-8 -*-
'''
@File : Fibonacci.py
@Time : 2020/03/06 18:10:07
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
filist=[0,1]
i=1
while (i==1):
    filist.append(filist[-1]+filist[-2])
    if(filist[-1]>100):
        del(filist[-1])
        break
print(filist)