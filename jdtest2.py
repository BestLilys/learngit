#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   jdtest2.py
@Time    :   2020/05/20 15:46:43
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os,random
from collections import Counter
def main():
    path=input('请输入生成文档路径:')
    path=os.path.join(path,'ip.txt')
    with open(path,'w')as f1:
        for i in range(1200):
            id=str(random.randint(1,254))
            f1.writelines('172.25.254.%s\n'%id)
    with open (path,'r')as f2:
        iplist=f2.readlines()
        ipcommon=Counter(iplist).most_common(10)
        for ip in ipcommon:
            print(ip[0].strip('\n'))
if __name__ == "__main__":
    main()