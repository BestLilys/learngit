# -*- encoding: utf-8 -*-
'''
@File : countamount.py
@Time : 2020/03/06 22:09:17
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
import re
string=input('请输入英文文本:')
mylist_a=re.split('[,!?;:. ]',string)
mydict={}
for i in mylist_a:
    if(i==''):
        continue
    elif(i in mydict):
        mydict[i]=mydict[i]+1
    else:
        mydict[i]=1
mylist_b=sorted(mydict.items(),key=lambda x:x[1])
print(mylist_b)