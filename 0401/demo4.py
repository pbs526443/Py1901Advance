import types

class Good():
    # __slots__会限制添加属性，如果动态的添加属性里slots没有就会报错
    __slots__ = ('addr','name','pwd','geti')
    def __init__(self,_addr):
        self.addr = _addr


a1 = Good("asd")
print(a1.addr)

# 动态添加类属性
Good.name = "qwe"
print(Good.name)
print(a1.name)

# 动态添加实例属性
a1.pwd = "123"
print(a1.pwd)

# __slots__里没有attack,所以会报错
# a1.attack = 100
# print(a1.attack)

# 定义实例方法
def getinfo(self):
    print("move")

# 动态的添加实例方法
a2 = Good("fujian")
a2.geti = types.MethodType(getinfo,a2)
a2.geti()

# 定义类方法
@classmethod
def getdoc(cls):
    print(cls.__doc__)
# 动态的添加类方法
Good.getd = getdoc
Good.getd()
a2.getd

# 定义静态方法
@staticmethod
def get():
    print("staric method")
#动态的添加静态方法
Good.get1 = get
Good.get1()

# 删除指定属性
delattr(Good,"get1")
if hasattr(Good,"get1"):
    print("存在get")
else:
    print("不存在get1")

# del a2.geti
if hasattr(a2,"geti"):
    print("存在geti")
else:
    print("不存在geti")