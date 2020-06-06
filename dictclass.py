#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   dictclass.py
@Time    :   2020/06/05 17:28:53
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
class dictclass():
    def __init__(self,dic):
        self.mydict=dic
    def del_dict(self,key):
        del self.mydict[key]
    def get_dict(self,key):
        if key in self.mydict:
            return self.mydict[key]
        else:
            return 'not found'
    def get_key(self):
        mylist=[]
        for i in self.mydict:
            mylist.append(i)
        return mylist
    def update_dict(self,condict):
        relist=[]
        for i in condict:
            if i in self.mydict:
                self.mydict[i]=self.mydict[i]+condict[i]
            else:
                self.mydict[i]=condict[i]
        for i in self.mydict:
            relist.append(self.mydict[i])
        return relist
def main():
    dict1=dictclass({'1':5,'2':10,'3':19})
    dict1.del_dict('1')
    print(dict1.get_dict('2'))
    print(dict1.get_key())
    print(dict1.update_dict({'4':1,'3':1,'1':2}))
if __name__ == "__main__":
    main()