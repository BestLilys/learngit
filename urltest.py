#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   urltest.py
@Time    :   2020/05/20 16:29:03
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import requests,os
def getimg(url,path):
    img=requests.get(url)
    path=os.path.join(path,name+'.jpg')
    with open(path,'wb') as f:
        f.write(img.content)
    print('图片保存成功')
if __name__ == "__main__":
    url=input('请输入下载的图片网址:')
    path=input('请输入保存图片位置:')
    name=input('请输入保存图片的名称:')
    getimg(url,path)

