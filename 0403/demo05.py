'''
通过sys getrefcount(obj)
'''

from sys import getrefcount

print(getrefcount("hello"))
a= "hello"
print(getrefcount("hello"))
b = "hello"
print(getrefcount("hello"))
c = a
print(getrefcount("hello"))
c = "world"
print(getrefcount("hello"))
del  b
print(getrefcount("hello"))

def fun (pam):
    print(pam)
    print(getrefcount(pam))


fun("hello")
print(getrefcount("hello"))

print("------------------------------------")

list1 = [1,2,3]
list2 = [4,5,6]
print(getrefcount([1,2,3]))
print(getrefcount(list1))
print(getrefcount(list2))
list1.append(list2)
list2.append(list1)
print(getrefcount([1,2,3]))
print(getrefcount(list1))
print(getrefcount(list2))
del list1
print(getrefcount([1,2,3]))
print(getrefcount([4,5,6]))
print(getrefcount(list2))
print(list2[3])
del list2
print(getrefcount([4,5,6]))
print(getrefcount([4,5,6]))

'''
原始存储[1,2,3]内存块A    [4,5,6]存储在内存块B    内存引用计数1
list1 = 内存A    内存A + 1 => 2
list2 = 内存B    内存B + 1 => 2

循环引用导致内存A+1 => 3   内存B + 1 => 3
del list1   内存A-1 => 2
del list2   内存B-1 => 2

内存A 和 内存B 比原始状态 引用计数+1

第一个缺点: 维护所有内存的引用计数 消耗资源
第二个缺点：当循环引用时导致内存泄漏
'''
