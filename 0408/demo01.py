# 1 导入模块
import logging,json
# # 2 创建日志模块
# logingLogin = logging.getLogger('main')
# # 2.1 设置等级
# logingLogin.setLevel(logging.DEBUG)
# # 3 创建日志输出类型
# fileHandler = logging.FileHandler('loginregist.txt',encoding='utf-8')
# # 3.1 文件日志等级
# fileHandler.setLevel(logging.ERROR)
# # 4 指定日志格式
# fileformater = logging.Formatter('%(name)s-%(levelno)s-%(lineno)d-%(asctime)s-%(message)s')
# # 5 将文件绑定日志格式
# fileHandler.setFormatter(fileformater)
#
# # 输出到控制台使用StreamHandler()
# streamHandler = logging.StreamHandler()
# streamHandler.setLevel(logging.INFO)
# streamHandler.setFormatter(fileformater)
#
# # 6 将日志处理方法添加到日志工具
# logingLogin.addHandler(fileHandler)
# logingLogin.addHandler(streamHandler)
#
# logingLogin.debug('debug')
# logingLogin.info('info')
# logingLogin.warning('warning')
# logingLogin.error('error')


class Good():
    def __init__(self,_name,_price):
        self._name = _name
        self._price = _price

# g = Good()
# g.name = input('请输入商品名：')
# g.price = input('商品价格：')

with open('good.txt','w') as f:
    name = input('商品名称：')
    price = input('数量：')
    g = Good(name,price)
    result = json.dumps(g.__dict__)
    print(result,type(result))
    f.write(result)

with open('good.txt','r') as f:
    content = f.read()
    g =  json.loads(content)
    print(g)




# list1 = [1,2,3,4,5,6]
#
# def fun(x):
#     return x
#
# l1 = filter(fun,list1)
# for r in l1:
#     print(r)