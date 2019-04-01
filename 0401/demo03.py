'''
实例方法：需要第一个参数为self
类方法：需要第一个参数为cls，并且使用@classmethod声明
静态方法：需要使用@staticmethod声明

类可以调用，类方法，静态方法
实例可以调用，类方法，静态方法，实例方法
'''
class Good():
    '''
    这是一个商品类
    '''
    addr = 'fujian'

    def __init__(self,_name):
        self.name = _name

    def getname(self):
        return self.name

    @staticmethod
    def dead():
        print("商品")

    @classmethod
    def printclassinfo(cls):
        print("类方法")

# 实例属性,实例可以调用类方法
a1 = Good(10)
print(a1.name,a1.addr)

# 类属性
Good.addr = 'zhongguo'
print(Good.addr)

# 调用实例方法
a2 = a1.getname()
print(a2)

# 调用静态方法
a1.dead()

# 调用类方法
a1.printclassinfo()