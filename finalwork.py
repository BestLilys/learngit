#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   finalwork.py
@Time    :   2020/06/25 10:06:52
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
import requests
import re
from queue import Queue
from bs4 import BeautifulSoup
import mysql.connector
import threading
HEADERS = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
    "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}
original_url='https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
threadLock=threading.Lock()
threads=[]
queue=Queue()
for i in range(1,39):
    queue.put(original_url.format(i))
class JobGet(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.joblist= []
    def ave_salary(self):
        salary_list=[]
        count=0
        s=0
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            db="job_database"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT salary FROM job_list where jlocation like '%北京%'")
        myresult=mycursor.fetchall()
        for x in myresult:
            count=count+1
            result_list=re.findall(r"\d+\.?\d*",x[0])
            if '万/月' in x[0]:
                s=s+(float(result_list[0])+float(result_list[1]))*12
            elif '万/年' in x[0]:
                s=s+float(result_list[0])+float(result_list[1])
            elif '千/月' in x[0]:
                s=s+((float(result_list[0])+float(result_list[1]))/10)*12
        return s/(count*2)
    def db_create(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
        )
        mycursor=mydb.cursor()
        mycursor.execute("CREATE DATABASE job_database")
    def db_insert(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            db="job_database"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE job_list(job VARCHAR(50),jlocation varchar(50) ,salary varchar(50));")
        sql="INSERT INTO job_list(job,jlocation,salary) VALUES(%s,%s,%s)"
        for j in range(len(self.joblist)):
            val=(self.joblist[j]['job'],self.joblist[j]['location'],self.joblist[j]['salary'])
            mycursor.execute(sql,val)
            mydb.commit()
    def run(self):
        while queue.qsize()>0:
            threadLock.acquire()
            url=queue.get()
            response=requests.get(url,headers=HEADERS)
            if response.status_code==200:
                html = response.content.decode("gbk")
            else:
                queue.put(url)
                continue
            bs = BeautifulSoup(html, "lxml").find("div", class_="dw_table").find_all(
                "div", class_="el"
            )
            for b in bs:
                try:
                    job = b.find("a")["title"]
                    location = b.find("span", class_="t3").text
                    salary = b.find("span", class_="t4").text
                    item = {
                        "job":job, "location": location, "salary": salary
                    }
                    self.joblist.append(item)
                except Exception:
                    pass
            threadLock.release()
        self.db_create()
        self.db_insert()
        print(r'北京地区平均工资:%.1f万/年'%(self.ave_salary()))
if __name__ == "__main__":
    project1=JobGet()
    project2=JobGet()
    project3=JobGet()
    project4=JobGet()
    project5=JobGet()
    project1.start()
    project2.start()
    project3.start()
    project4.start()
    project5.start()
    threads.append(project1)
    threads.append(project2)
    threads.append(project3)
    threads.append(project4)
    threads.append(project5)
    for t in threads:
        t.join()
    
