# -*- encoding: utf-8 -*-
'''
@File : 列表问题.py
@Time : 2020/03/05 22:55:31
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
list1=['Leon','Linda','Chris','Ada','Clare']
list2=['Tom','Jerry','Leon','Ada']
print('相同的元素有:',end='')
for i in list1:
    if(list2.count(i)>0):
        print(i,end=' ')