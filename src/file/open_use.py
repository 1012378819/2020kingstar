# f=open(r'C:\txt\somefile.txt')  #linux: '~/sometxt'
file='data_files\data.txt'
f=open(file,'w') #默认模式为r，只读，还有a，appending，追加不覆盖，w是覆盖
f.write("012345678")  #写
f.seek(5) #
f.write("hello, world!")
f.close()
f=open(file)
print(f.read(8))
print(f.read())
print('再读：',f.read()) # f.read()已经读到尾部，再读就是空
f.close()

# with open('a.txt') as somefile:
#     do_sth(somefile)

file_s='data_files\s.txt'
def A():
    f=open(file_s)
    while True:
        char=f.read(1)
        if not char:
            break
        print(char)
    f.close()
# A()
def B():
    f=open(file_s)
    while True:
        line=f.readline()
        if not line:
            break
        print(line)
    f.close()
# B()
def C():
    f=open(file_s)
    for char in f.read():
        print(char)
    f.close()
# C()
def D():
    f=open(file_s,encoding='utf-8')
    for line in f.readlines():
        print(line)
    f.close()

# D()

# #py2.2版本后，文件对象可迭代
for line in open('data_files\s.txt',encoding='utf-8'):
    print(line)