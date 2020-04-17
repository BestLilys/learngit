#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   countword.py
@Time    :   2020/04/17 22:23:01
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import os,re
def readtext(filename):
    worddict={}
    with open (filename,'r',encoding='utf-8') as f:
        txt=f.read(2000)
        txt=txt.lower()
        wordlist=re.split(r'[}{\;?<>:|,./~! @$%^&*"\n()“”-]',txt)
        for word in wordlist:
            if(word not in worddict and word!=''):
                worddict[word]=wordlist.count(word)
    return worddict
worddict=readtext('text.txt')
wordlist=[]
for word in worddict:
    wordlist.append((word,worddict[word]))
wordlist.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    print(wordlist[i][0],end='  ')
