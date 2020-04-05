def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

def lookup(data,lable,name):
    return data[lable].get(name)

def store(data,full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,'')
    lables=('first','middle','last')
    for lable,name in zip(lables,names):
        people=lookup(data,lable,name)
        if people:
            people.append(full_name)
        else:
            data[lable][name]=[full_name]  #这边需要存为list，list才有append方法，把相同首中尾相同的存在一起

def store_2(data,*full_names):
    for full_name in full_names:
        store(data,full_name)
        # names=full_name.split()
        # if len(names)==2:
        #     names.insert(1,'')
        # lables=('first','middle','last')
        # for lable,name in zip(lables,names):
        #     people=lookup(data,lable,name)
        #     if people:
        #         people.append(full_name)
        #     else:
        #         data[lable][name]=[full_name]  #这边需要存为list，list才有append方法，把相同首中尾相同的存在一起

def test():
    MyNames={}
    MyNames_2={}
    init(MyNames)
    init(MyNames_2)
    store(MyNames,'zhang san feng')
    store(MyNames,'lu pei')
    store(MyNames,'jia chen')
    store_2(MyNames_2,'zhang san feng','zhang xiao huang','zhang hua')
    print(lookup(MyNames,'middle','san'))
    print(lookup(MyNames,'middle',''))
    print(lookup(MyNames_2,'first','zhang'))

# test()





