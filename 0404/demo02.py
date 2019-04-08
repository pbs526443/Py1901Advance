'''
由re.compile
'''
import re
# 得到匹配模式
s1 = "helloworld\nhid\nHello worlld"
print(s1)
# pat = re.compile('.',re.I|re.M)
# pat = re.compile('..d$',re.I|re.M)
# pat = re.compile('he',re.I|re.M)
pat = re.compile('.',re.S)
result = pat.findall(s1)
print(result,type(result))