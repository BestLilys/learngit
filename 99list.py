# -*- encoding: utf-8 -*-
'''
@File : 99list.py
@Time : 2020/03/06 18:25:55
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(j,i,j*i),end=' ')
    print('\n')
