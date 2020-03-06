# -*- encoding: utf-8 -*-
'''
@File : stuffproblem.py
@Time : 2020/03/06 21:18:56
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
mylist=[]
mylist.append(('1','Leon',2,15000))
mylist.append(('2','Ada',3,20000))
mylist.append(('3','Chris',4,13000))
mylist.append(('4','Clare',2,10000))
mylist.append(('5','Sherly',1,9000))
mylist.append(('6','Tom',5,30000))
mylist.append(('7','Jerry',5,25000))
mylist.append(('8','Andy',3,8000))
mylist.append(('9','Jack',1,9000))
mylist.append(('10','Mary',3,14000))
mylist.sort(key=lambda x:x[3])
print(mylist)
