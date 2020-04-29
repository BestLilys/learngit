#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   count2.py
@Time    :   2020/03/09 20:31:10
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
def count2(string):
    sumint=sumal=sumspace=sumother=0
    for i in string:
        if(i>='0' and i<='9'):
            sumint+=1
        elif((i>='a' and i<='z') or (i>='A' and i<='Z')):
            sumal+=1
        elif(i==' '):
            sumspace+=1
        else:
            sumother+=1
    print('数字:{} 字母:{} 空格:{} 其他:{}'.format(sumint,sumal,sumspace,sumother))
mystr=input('请输入字符串:')
count2(mystr)
            
