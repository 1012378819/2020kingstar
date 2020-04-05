# -*- coding: utf-8 -*-
"""
@time: 2020/2/11 14:12
@author: pei.lu
"""
# 非对称加密算法rsa
import rsa
# # 生成公钥、私钥
# public_key,private_key=rsa.newkeys(1024)
# # 保存公钥到u盘
# with open('public_huk.pem', 'w') as fp:
#     fp.write(public_key.save_pkcs1().decode()) # decode():字节码转字符串
# # 保存私钥到浩克的电脑上
# with open('private_huk.pem', 'w') as fp:
#     fp.write(private_key.save_pkcs1().decode())

"""加密"""
message='绝对不能让第三者知道！'
# 导入公钥
with open('public_huk.pem', 'r') as f:
    pubkey=rsa.PublicKey.load_pkcs1(f.read().encode()) # encode()字符串转字节码
#使用公钥加密信息
crypto=rsa.encrypt(message.encode('utf-8'),pubkey)
# print(crypto)
"""解密"""
# 导入私钥
with open('private_huk.pem', 'r') as f:
    privkey=rsa.PrivateKey.load_pkcs1(f.read().encode())

res_message=rsa.decrypt(crypto,privkey).decode('utf-8')
print(res_message)


############分割线#############
# 数字签名
message='按兵不动，不露声色'
# 导入私钥
with open('private_huk.pem','r') as f:
    privkey=rsa.PrivateKey.load_pkcs1(f.read().encode())

# 生成摘要
digest=str(hash(message.encode('utf-8')))
# 生成签名
signature=rsa.encrypt(digest,privkey)
# 加密邮件内容
crypto=rsa.encrypt(message.encode('utf-8'),privkey)

##验证数字签名（见图）
# 导入公钥
with open('public_huk.pem') as f:
    pubkey=rsa.PublicKey.load_pkcs1(f.read().encode())
# 解密邮件内容：按兵不动，不露声色
message=rsa.decrypt(crypto,pubkey).decode('utf-8')
# 生成摘要1
digest1=str(hash(message.encode('utf-8')))
# 解密数字签名，得到生成摘要0
digest0=rsa.decrypt(signature,pubkey)
if digest0==digest1:
    print(message)








