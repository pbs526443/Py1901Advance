'''
输入：字符串
输出：None,match对象
match：字符串开头匹配，成功返回match对象，否则为None
search：扫描整个字符串，找到与pattern的第一个匹配，并返回一个对应的match，否则为None
fullmatch：判断是string是否与pattern整个相同，如果是就返回match对象，否则为None
findall：将匹配到的返回一个列表
split：将匹配到与pattern的字符进行分割，并返回一个列表
sub：使用repl替换pattern匹配到的内容，最多匹配count次
finditer：返回一个迭代器
compile：编译得到匹配模型
'''
import re
s1 = 'hello world'
# result = re.match('hello',s1)
result = re.search('o',s1)
# result = re.fullmatch('hello world',s1)
# result = re.findall('l',s1)
# result = re.split('ll',s1)
# result = re.sub('ll','6666',s1)
# result = re.finditer('l',s1)
# print(next(result))
# result = re.compile('hello')
# print(result,type(result))
if result:
    if isinstance(result,re.Match):
        # group 获取match对象的值
        print(result.group())
        print(result,type(result))
    else:
        for x in result:
            print(x)