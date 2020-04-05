# -*- coding: utf-8 -*-
#@time: 2019/12/1 20:55
#@author: pei.lu
# 文件分类保存任务

def save_file(boy,girl,count):
    boy_file_name='boy_'+str(count)+'.txt'
    girl_file_name='girl_'+str(count)+'.txt'
    b=open(boy_file_name,'w')
    g=open(girl_file_name,'w')
    b.writelines(boy)
    g.writelines(girl)
    b.close()
    g.close()
    
def split_file(file):
    f=open(file,encoding='utf-8')
    boy=[]
    girl=[]
    count=1
    for item in f:
        if item[:6]!='='*6:
            (name,content)=item.split(':',1)
            if name=='A':
                boy.append(content)
            elif name=='B':
                girl.append(content)
        else:
            save_file(boy,girl,count)
            boy=[]
            girl=[]
            count+=1
    save_file(boy,girl,count)    
    f.close()  
            
split_file('dialogue.txt')       