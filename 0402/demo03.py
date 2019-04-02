from collections.abc import Iterator,Iterable
# Iterator 迭代器：可以使用next方法
# Iterable可迭代：可以使用for循环遍历
# 生成器既是可迭代，又是迭代器

# list1 = [1,2,3,4]
# print(isinstance(list1,Iterator))
# print(isinstance(list1,Iterable))
#
# dict1 = {"name":"qwe","age":23}
# print(isinstance(dict1,Iterator))
# print(isinstance(dict1,Iterable))
#
# print(isinstance((x for x in range(10)),Iterator))
# print(isinstance((x for x in range(10)),Iterable))
#
# print(isinstance('asd',Iterator))
# print(isinstance('asd',Iterable))
#
# # iter()函数可以使Iterable 变成 Iterator
# print(isinstance(iter(list1),Iterator))
# print(isinstance(iter(list1),Iterable))

class Good():
    def __init__(self,_addr):
        self.addr = _addr
        self.num = 0

    def __iter__(self):
        return  self

    def __next__(self):
        if self.num < len(self.addr):
            result = self.addr[self.num]
            self.num += 1
            return result
        else:
            return print("越界引发异常")
            # try:
            #     return print("越界引发异常")
            # except StopIteration as e:
            #     print(e)

g1 = Good(["hainan","henan","hebei"])
# print(g1,type(g1))
print(g1.__next__())
print(g1.__next__())
print(g1.__next__())
print(g1.__next__())