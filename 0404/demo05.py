'''
^ 开头 包括字符串的原始开头 多行模式下 \n后面的内容
$ 结尾 包括字符串最后 \n前面内容
\b 代表单词边界  只能用于原始字符串 符号. \n也算空
\B 代表非单词边界
'''

import re
result = re.findall('^hello','hello world\nhello zhengzhou',re.M)
print(result)

result = re.findall('zhengzhou$','hello world zhengzhou\nhello zhengzhou',re.M)
print(result)

# \b表示回退，一定要使用原始语句r
result = re.findall(r'\bhello','hello world\nhello zhengzhou',re.M)
print(result)

result = re.findall('\Bhello','ahello world\nahello zhengzhou',re.M)
print(result)


result = re.findall(r'\bhello\b|\bhi\b|\bworld\b','hello world\nhi hello zhengzhou',re.M)
print(result)

# result = re.findall(r'he(.*?)o(.*?)o','hello world\nhello zhengzhou',re.M)
result = re.search(r'he(.*?)o(.*?)o','hello world\nhello zhengzhou')
print(result.group(),result.group(1),'++++++++',result.group(2))

result = re.match(r'(hello).*?\1','hello world hello zhengzhou')
print(result.group(),result.group(1))

result = re.search(r'(?P<hname>world).*?(?P=hname)','hello world hello world zhengzhou')
print(result.group(),result.group(1),'++++++++',result.group('hname'))

'''
| 代表左右任意一个满足即可
'''
