'''
* >=0
+ >=1
? 0/1
{m} =m
{m,} >=m
{m,n} m<=x<=n

正则表达式默认是贪婪模式，即尽可能的多匹配
？表示开启非贪婪模式，即尽可能的少匹配（有0则0，有1则1）
'''

import re

result = re.findall('hi*','hi china hello chiina')
print(result)

result = re.findall('hi*?','hi china hello chiina')
print(result)

result = re.findall('hi+','hi china hello china')
print(result)

result = re.findall('hi+?','hi china hello china')
print(result)

result = re.findall('hi?','hi china hello chiina')
print(result)

result = re.findall('hi??','hi china hello china')
print(result)

result = re.findall('hi{2}','hi china hello chiina')
print(result)

result = re.findall('hi{1,}','hi china hello chiina')
print(result)

result = re.findall('hi{1,}?','hi china hello china')
print(result)

result = re.findall('hi{0,2}','hi china hello china')
print(result)

result = re.findall('hi{0,2}?','hi china hello china')
print(result)