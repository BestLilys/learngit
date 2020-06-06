#!/usr/bin/python3
#encoding:utf-8
'''
@File    :   studentcontrol.py
@Time    :   2020/06/06 16:04:28
@Author  :   Best_Lilys 
@Version :   1.0
@Contact :   2429715377@qq.com
@WebSite :   https://github.com/BestLilys
'''
# Start typing your code from here
class studentcontrol():
    def __init__(self,path):
        self.path=path
    def add_info(self):
        cas=input('请输入班级:')
        name=input('请输入姓名:')
        learnid=input('请输入学号:')
        pyscore=int(input('请输入python分数:'))
        with open (self.path,'a') as f:
            f.write('%s %s %s %d\n'%(cas,name,learnid,pyscore))
    def del_info(self):
        name=input('请输入删除学生名字:')
        with open(self.path,'r') as f:
            infolist=f.readlines()
        for i in range(0,len(infolist)):
            if name in infolist[i]:
                del infolist[i]
                break
        else:
            print('没有此学生')
        with open (self.path,'w') as f:
            f.writelines(infolist)
    def change_info(self):
        name=input('请输入要修改的学生姓名:')
        keys=input('请输入要修改的字段:').split()
        info=input('请输入各字段分别要修改的信息:').split()
        with open(self.path,'r') as f:
            infolist=f.readlines()
        for i in range(0,len(infolist)):
            if name in infolist[i]:
                thisinfolist=infolist[i].split()
                del infolist[i]
                break
        else:
            print('没有此学生')
        for i in range(0,len(keys)):
            if keys[i]=='班级':
                thisinfolist[0]=info[i]
            if keys[i]=='姓名':
                thisinfolist[1]=info[i]
            if keys[i]=='学号':
                thisinfolist[2]=info[i]
            if keys[i]=='python分数':
                thisinfolist[3]=info[i]+'\n'
        infolist.append(' '.join(thisinfolist))
        with open(self.path,'w')as f:
            f.writelines(infolist)
    def search_info(self):
        name=input('请输入要查询学生名字:')
        with open(self.path,'r') as f:
            infolist=f.readlines()
        for i in infolist:
            if name in i:
                print(i[:-1])
                break
        else:
            print('没有此学生')
def main():
    student=studentcontrol(r'E:\pyproject\project1\123\student.txt')
    student.add_info()
    student.add_info()
    student.change_info()
    student.search_info()
    student.del_info()
    student.search_info()
if __name__ == "__main__":
    main()
        


