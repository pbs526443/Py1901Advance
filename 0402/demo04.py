'''
闭包：
函数的内部声明函数
外部函数返回内部函数的应用
内部函数可以访问外部函数局部变量

'''


def fun1(a):
    def fun2(b):
        nonlocal a
        a += 1
        return a+b
    return fun2

f = fun1(10)
print(type(f))
print(f(10))
print(f(20))

from demo05 import selectgoods

selectgoods()
