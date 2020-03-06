# -*- encoding: utf-8 -*-
'''
@File : 字典问题.py
@Time : 2020/03/05 22:34:52
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
dic={'101':90,'102':92,'103':91,'104':90,'105':76,'106':87,'107':94,'108':98,'109':64,'110':89}
for i in dic:
    if(dic[i]>80):
        print('({0},{1})'.format(i,dic[i]),end='  ')