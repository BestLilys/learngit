# -*- encoding: utf-8 -*-
'''
@File : cncount.py
@Time : 2020/04/28 15:12:56
@Author : Best_Lilys
@Version : 1.0
@Contact : 2429715377@qq.com
@WebSite : github.com/BestLilys
'''

# here put the import lib
import jieba,re
from collections import Counter
with open('text.txt','r',encoding='utf-8') as f:
    text=re.sub(r'[，。？；,.?;\n]','',f.read())
    wordlist=jieba.lcut(text)
    result=Counter(wordlist)
    keylist=result.most_common(10)
for i in keylist:
    print(i[0])
