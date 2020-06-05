#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   dog.py
@Time    :   2020/06/05 16:13:22
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
class dog():
    colordict={'1':'白','2':'黄','3':'黑'}
    numdict={'1':5,'2':5,'3':5}
    pricedict={'1':500,'2':300,'3':400}
    def __init__(self):
        self.doglist=[self.colordict,self.numdict,self.pricedict]
    def perchase(self):
        color=input('想要哪种颜色的狗(白/黄/黑):')
        for i in self.colordict:
            if self.colordict[i]==color:
                num=int(input('还有{}只,想要买几只:'.format(self.numdict[i])))
                if num<=self.numdict[i]:
                    print('交易成交，共支付{}元'.format(num*self.pricedict[i]))
                    self.numdict[i]=self.numdict[i]-num
                    break
                else:
                    print('数量不够,交易失败')
        else:
            print('无此颜色狗')    
def main():
    dogperchase=dog()
    dogperchase.perchase()
    dogperchase.perchase()
    for i in dogperchase.numdict:
        print('{}色狗还有{}只'.format(dogperchase.colordict[i],dogperchase.numdict[i]))
if __name__ == "__main__":
    main()




