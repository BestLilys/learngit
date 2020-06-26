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
        self.list_name=''
        self.database_name=''
        self.User=''
        self.password=''
    def ave_salary(self):
        salary_list=[]
        count=0
        s=0
        mydb = mysql.connector.connect(
            host="localhost",
            user=self.User,
            passwd=self.password,
            db=self.database_name
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT salary FROM {} where jlocation like '%北京%'".format(self.list_name))
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
        self.User=input('请输入连接数据库的用户名:')
        self.password=input('请输入连接数据库的密码:')
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user=self.User,
            passwd=self.password,
            )
            mycursor=mydb.cursor()
            self.database_name=input('请输入创建的数据库名:')
            mycursor.execute("CREATE DATABASE %s"%(self.database_name))
        except Exception:
            print('密码错误!')
    def list_create(self):
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user=self.User,
            passwd=self.password,
            db=self.database_name
            )
            mycursor=mydb.cursor()
            self.list_name=input('请输入创建的表名:')
            mycursor.execute("CREATE TABLE %s(job VARCHAR(50),jlocation varchar(50) ,salary varchar(50));"%(self.list_name))
        except Exception:
            print('密码错误!')
    def db_insert(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=self.User,
                passwd=self.password,
                db=self.database_name
            )
            mycursor = mydb.cursor()
            sql="INSERT INTO {}(job,jlocation,salary) VALUES(%s,%s,%s)".format(self.list_name)
            for j in range(len(self.joblist)):
                val=(self.joblist[j]['job'],self.joblist[j]['location'],self.joblist[j]['salary'])
                mycursor.execute(sql,val)
                mydb.commit()
        except Exception:
            print('创建表失败!')
    def job_get(self,tname):
        print('{}:正在爬取,请稍等!'.format(tname))
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
if __name__ == "__main__":
    project=JobGet()
    project.db_create()
    project.list_create()
    for i in range(5):
        t=threading.Thread(target=project.job_get('线程%d'%(i+1)))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    try:
            project.db_insert()    
            print('爬取成功，数据存储在{}数据库中的{}表中'.format(project.database_name,project.list_name))
            print(r'北京地区平均工资:%.1f万/年'%(project.ave_salary()))
    except Exception:
        pass
