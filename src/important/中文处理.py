# 字符串通过编码转换为字节码，字节码通过解码转换为字符串
# str--->(encode)--->bytes，bytes--->(decode)--->str
import sys
str1 = '中文'
print(str1)
print(sys.getfilesystemencoding())
str2 = str1.encode(sys.getfilesystemencoding()) #对于python3默认的就是unicode编码。
print(str2)
str3=str2.decode('utf-8')  #解码，如果encode()和decode()括号中不写编码格式,系统会默认为utf-8
print(str3)

#py2 示例：列表或字典中的中文处理
#我们用print直接输出data, 或用str函数将data转为字符串。其中的中文是变成unicode的字符，如：
data = {"a":"hello","b":"中国"}
print(data)  #{'a': 'hello', 'b': '\xd6\xd0\xb9\xfa'}
print(data['b'])  #中国

# 如果希望能正常的将整个字典输出，可以利用json包的dump方法，如：
# >>> data = {"a":"hello","b":"中国"}
# >>> s = json.dumps(data,ensure_ascii=False);
# >>> print s
# {"a": "hello", "b": "中国"}
# >>> print isinstance(s,str)
# True
