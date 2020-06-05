#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   student6.py
@Time    :   2020/06/05 16:43:45
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
class student():
    name='Leon'
    age=18
    score=(100,100,100)
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.score=s
    @classmethod
    def get_name(cls,self):
        return self.name
    @classmethod
    def get_age(cls,self):
        return self.age
    @classmethod
    def get_course(cls,self):
        return max(self.score)
def main():
    student1=student('Jerry',19,(99,99,99))
    print('姓名:{}  年龄:{}  最高分:{}'.format(student.get_name(student1),student.get_age(student1),student.get_course(student1)))
if __name__ == "__main__":
    main()
