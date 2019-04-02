'''
函数式生成器
通过函数+yield

yield 可以保存当前函数状态并继续执行
每一次yield向当前生成器插入对象

函数返回值变成生成器
可以使用异常捕获得到函数return语句返回值
'''
import sys

def fun():
    yield 1
    yield 2
    yield 3
    return 'hello'

print(type(fun()))
print(next(fun()))

g = fun()
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except Exception as e:
    print(e)

def fib(times):
    n = 0
    a,b = 0,1
    yield a
    yield b
    while n<times:
        a,b = b,a+b
        yield b
        n +=1
    print("finish")
r = fib(10)
while True:
    try:
        print(next(r))
    except Exception as e:
        print(e)
        break
