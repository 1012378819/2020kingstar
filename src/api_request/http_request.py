# -*- coding:utf-8 -*-
#@time: 2019/11/22 14:10
#@author: pei.lu
import requests,json
# url=''
# requests.get(url)
class HttpRequest:
    def http_request(self,url,data,method="POST"):
        if method.upper()=="GET":
            res=requests.get(url,data)
        else:
            res=requests.post(url,data)
        return res.text


# funcno=31001006;url=http://10.243.141.53:9020/angel/angel/pray.req;
# data="m":"20010012","f":"31001006","u":"superAdmin","a":"uniauth","k":"","n":"superAdmin201707171118011009","s":{"n":["p_auth_type","p_auth_code","p_auth_name","p_auth_state","p_auth_effect","p_auth_expire","p_page_count","p_page_no"],"v":["1","","","","","","10","1"]},"x":True,"y":False
if __name__ == '__main__':
    url='http://10.253.47.204:16679/service/v001/adaptor/customSign'
    str_data="""{
 "userInfo":{
  "clientId":"ad_auto01"
 },
 "deviceInfo":{

 },
 "riskInfo":{

 },
 "data":{
  "tradeChannel":2,
  "custType":2,
  "openBank":"ad_auto01bank",
  "accountName":"ad_auto01name",
  "cardNo":"ad_auto01card",
  "riskLevel":"ad_auto01",
  "cardPhone":"15999012201",
  "userGradeCd":"9"
 }
}"""
    json_data = {
     "userInfo":{
      "clientId":"ad_auto03"
     },
     "deviceInfo":{

     },
     "riskInfo":{

     },
     "data":{
      "tradeChannel":2,
      "custType":2,
      "openBank":"ad_auto01bank",
      "accountName":"ad_auto01name",
      "cardNo":"ad_auto01card",
      "riskLevel":"ad_auto01",
      "cardPhone":"15999012201",
      "userGradeCd":"19"
     }
    }
    headers={"Content-Type":"application/json;charset=UTF-8"}
    # res=requests.post(url,data=str_data,headers=headers)   # data是字符串数据的方式进行请求
    # res=requests.post(url,data=json.dumps(json_data),headers=headers) # data是json的方式，进行下json数据处理成str然后请求
    res=requests.post(url,json=json_data,headers=headers) # 直接给json参数赋值的方式进行请求
    print(res.text,sep='\n')
    print(json.loads(res.text),sep='\n') # 得到字符串返回值，处理成json然后再后续操作
    print(json.loads(res.text)['responseMsg'])