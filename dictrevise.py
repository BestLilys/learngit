#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   dictrevise.py
@Time    :   2020/03/09 21:07:54
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
def dictrevise(mydict):
    for i in mydict:
        if(isinstance(mydict[i],int)):
            while(mydict[i]>99):
                mydict[i]=int(mydict[i]/10)
        elif(len(mydict[i])>2):
            mydict[i]=mydict[i][:2]
    print(mydict)
mydict={'Leon':'asdnzxc','Ada':'cxzndsa','Chris':123341}
dictrevise(mydict)