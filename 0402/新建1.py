
list1 = (x for x in range(10))

# while 循环
while True:
    try:
        h = next(list1)
        print(h)
    except Exception as e:
        print(e)
        break
# for 循环
for i in list1:
    print(i)

# 裴波拉契数列
def fun(item):
    n = 0
    a,b = 0,1
    yield a
    yield b
    while n<item:
        a,b = b,a+b
        yield b
        n += 1
    print("end")

r = fun(5)
while True:
    try:
        print(next(r))
    except Exception as e:
        print(e)
        break

def lun():
    yield 1
    yield 2
    yield 3
    return 'hello'

g = lun()
while True:
    try:
        h = next(g)
        print(h)
    except StopIteration as e:
        print(e)
        break



