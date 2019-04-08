
import re
# result = re.findall('.','hello\n world',re.S)
# result = re.findall('[1,2,3,4].ello','4hello\n world 1hello 2 world')
# result = re.findall('\d...','4hello\n world 1hello 2 world')
# result = re.findall('\Dhello','4hello\n world 1hello 2 world hhello')
result = re.findall('\s.hello','4hello\nworld 1hello hhello')
result = re.findall('\S.hello','4hello\nworld 1hello hhello ^hhello')
print(result)

