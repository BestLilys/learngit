# -*- encoding: utf-8 -*-
'''
@File : 闰年判断.py
@Time : 2020/03/05 23:03:32
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
i=int(input('请输入年份:'))
if (i%4==0):
    print("该年为闰年")
else:
    print("该年为平年")
