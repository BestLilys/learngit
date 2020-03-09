# -*- encoding: utf-8 -*-
'''
@File : guessnumber.py
@Time : 2020/03/06 21:52:50
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
import random
i=random.randint(1,21)
for n in range(1,6):
    j=int(input('请输入猜测的数字(1到20):'))
    if(j==i):
        print("猜对了!")
        break
    elif (j<i):
        print("猜小了!",end=' ')
    else:
        print("猜大了!",end=' ')
    print("还有{}次机会".format(5-n))
else:
    print("五次机会耗尽,猜测失败!")