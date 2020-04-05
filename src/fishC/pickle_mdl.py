# -*- coding:utf-8 -*-
'''
Created on 2019年12月22日

@author: pei.lu
'''
import pickle
city={'nanjing':'11','beijing':'12','shanghai':'13','nanjing':'11','yancheng':'12','xian':'13',
      'wuhan':'11','shantou':'12','shenzhen':'13','changsha':'11','hefei':'12','zhengzhou':'13'}
pickle_file=open('city_data.pkl','wb') # 二进制文件打开写存储
pickle.dump(city,pickle_file)
pickle_file.close()

pickle_file=open('city_data.pkl','rb') 
print(pickle.load(pickle_file))
