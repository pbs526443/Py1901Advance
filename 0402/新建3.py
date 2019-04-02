
def user(fun):
    def fun1():
        # 判断用户验证
        if input('输入用户名') == 'qwe':
            fun()
        else:
            print('权限错误')
    return fun1

# 调用user装饰器
@user
def text():
    print('商品信息')

text()

# 引入time模块
import time

def timecount(func):
    def num():
        # 获取开始前的时间
        a = time.time()
        func()
        # 获取结束后的时间
        b = time.time()
        print(b-a)
    return num

# 调用timecount
@timecount
def time1():
    # 创建一个list集合
    list1 = [x for x in range(100000)]
    print(list1.index(99999))

@timecount
def time2():
    # 创建一个生成器
    list2 = (x for x in range(100000))
    while True:
        try:
            # 获取值
            a = next(list2)
            # 判断值是否等于99999
            if a == 99999:
                print(a)
                break
        except StopIteration as e:
            print(e)
time1()
time2()