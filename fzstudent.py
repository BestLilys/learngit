#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   fzstudent.py
@Time    :   2020/06/06 14:36:21
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
class fzstudent():
    def __init__(self,n,a,g,es,ms,cs):
        self.__name=n
        self.__age=a
        self.__gender=g
        self.__es=es
        self.__ms=ms
        self.__cs=cs
    def __sum_score(self):
        return self.__ms+self.__cs+self.__es
    def __ave_score(self):
        return self.__sum_score/3
    def __print_info(self):
        print('姓名%s 年龄%d 性别%s 英语%d 数学%d 语文%d'%(self.__name,self.__age,self.__gender,self.__es,self.__ms,self.__cs))
def main():
    student1=fzstudent('Leon',20,'男',100,100,100)
if __name__ == "__main__":
    main()
