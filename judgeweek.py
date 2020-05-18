#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   judgeweek.py
@Time    :   2020/05/18 15:03:02
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
from datetime import datetime,timedelta
def weekjudge(year,month,day):
    date=datetime(year,month,day)
    firstday=datetime(year,1,1)
    weekdayf=firstday.weekday()+1
    daydelta=(date-firstday).days
    weekdelta=int(daydelta/7)
    if (daydelta%7)>(7-weekdayf):
        weekdelta+=1
    weekday=date.weekday()+1
    print('第{}周,周{}'.format(weekdelta,weekday))
def schoolweek(year,month,day):
    date=datetime(year,month,day)
    firstday=datetime(year,2,17)
    weekdayf=firstday.weekday()+1
    daydelta=(date-firstday).days
    weekdelta=int(daydelta/7)
    if (daydelta%7)>(7-weekdayf):
        weekdelta+=1
    weekday=date.weekday()+1
    print('开学第{}周,周{}'.format(weekdelta,weekday))
year,month,day=map(int,input('请输入日期(年月日以空格分隔):').split())
weekjudge(year,month,day)
schoolweek(year,month,day)