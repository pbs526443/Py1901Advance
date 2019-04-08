import requests,re

response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
# print(response.text)
content = response.text

result = re.search(r'<tbody class="tbody_right" id="datalist">(.*?)</tbody>',response.text,re.S)
result = re.findall(r'<tr>(.*?)</tr>',result.group(1))
# print(result)

with open('data.text','w',encoding='utf8') as f:
    for r in result:
        r1 = re.findall(r'<td.*?>(.*?)</td>', r)
        # print(r1[0],r1[1],r1[2])
        # id = re.findall('<a href="//stock.quote.stockstar.com/(.*?).shtml>(.*?)</a>',r1[0])
        id = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">\1</a>', r1[0])
        # print(id.group(1))
        name = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', r1[1])
        # print(name.group(2))
        age = re.search(r'<span class="red">(.*?)</span>', r1[2])
        print(age.group(1))
        info = "股票代码 " + str(id.group(1)) + " 股票名称 " + str(name.group(2)) + " 股票价格 " + str(age.group(1))
        f.write(info)
        f.write('\n')
# print(list)