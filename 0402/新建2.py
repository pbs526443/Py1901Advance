from collections.abc import Iterator,Iterable

list1 = [1,2,3]
print(isinstance(list1,Iterator))
print(isinstance(list1,Iterable))

list2 = (x for x in range(10))
print(type(list2))
print(isinstance(list2,Iterator))
print(isinstance(list2,Iterable))

tuple = (1,2,3)
print(isinstance(tuple,Iterator))
print(isinstance(tuple,Iterable))

dict = {'name':'qwe','age':23}
print(isinstance(dict,Iterator))
print(isinstance(dict,Iterable))

str = 'qwe'
print(isinstance(str,Iterator))
print(isinstance(str,Iterable))

it = 23
print(isinstance(it,Iterator))
print(isinstance(it,Iterable))