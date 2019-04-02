'''
装饰器：为了扩展函数功能，
由闭包+语法糖
@
'''

def check(fun):
    def ck():
        user = input("输入用户名:")
        if user == 'pbs':
            fun()
        else:
            print('无权限')
    return ck

# 在查询逻辑之前需要添加权限验证
@check
def selectgoods():
    print("封装查询商品逻辑")

# selectgoods()

# 将函数作为参数传递给装饰器 并且执行装饰器的返回
def checkuser(fun):
    # 只要发现装饰器语法就会执行
    # print('++')
    def check(*args):
        if input("请输入用户名:") == 'qwe':
            fun(*args)
        else:
            print("没有权限")
    return check

@checkuser
def showlist():
    for r in range(10):
        print(r)
@checkuser
def showdetail(num):
    print('当前页',num)
@checkuser
def list1():
    print("商品信息")

# showdetail(10)
# list1()

import time

def timecount(fun):
    def tc():
        start = time.time()
        fun()
        end = time.time()
        print(end-start)
    return tc
@timecount
def timelist1():
    list1 = [x for x in range(1000000)]
    print(list1.index(999999))

@timecount
def timelist2():
    list2 = (x for x in range(1000000))
    num = 0
    while True:
        try:
            h = next(list2)
            if h == 999999:
                print(h)
                break
            num += 1
        except StopIteration as e:
            print("没有")
timelist1()
timelist2()