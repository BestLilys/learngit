#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   humanvsdog.py
@Time    :   2020/06/06 14:55:38
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
from random import randint
class human(object):
    def __init__(self,n):
        self.name=n
        self.hp=100
        self.ak=10
    def attack(self,target):
        target.hp=target.hp-self.ak
        print('%s受到%s攻击,还剩%d血'%(target.name,self.name,target.hp))
        if target.hp<=0:
            print('%s死亡'%target.name)
            return 1
        return 0
class dog(object):
    def __init__(self,n):
        self.name=n
        self.hp=80
        self.ak=15 
    def attack(self,target):
        target.hp=target.hp-self.ak
        print('%s受到%s攻击,还剩%d血'%(target.name,self.name,target.hp))
        if target.hp<=0:
            print('%s死亡'%target.name)
            return 1
        return 0
def main():
    humans=[]
    humans.append(human('Leon'))
    humans.append(human('Ada'))
    dogs=[]
    dogs.append(dog('dog1'))
    dogs.append(dog('dog2'))
    dogs.append(dog('dog3'))
    i=randint(1,2)
    while len(humans)>0 and len(dogs)>0:
        if i%2==0:
            for j in range(0,len(humans)):
                n=0
                if len(dogs)>1:
                    n=randint(0,len(dogs)-1)
                if humans[j].attack(dogs[n])==1:
                    del dogs[n]
                    if len(dogs)==0:
                        break
        else:
            for j in range(0,len(dogs)):
                n=0
                if len(humans)>1:
                    n=randint(0,len(humans)-1)
                if dogs[j].attack(humans[n])==1:
                    del humans[n]
                    if len(humans)==0:
                        break
        i=i+1
    if len(humans)>0:
        print('狗团灭,人类胜利')
    else:
        print('人团灭，狗胜利')
if __name__ == "__main__":
    main()


    