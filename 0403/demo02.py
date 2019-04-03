# = 相当于引用
# list1 = [1,2,3,[4,5]]
# list2 = list1
# print(list1 is list2)
# print(list1[3] is list2[3])
# list1.insert(3,3.5)
# print(list1,list2)
# list2[4].insert(1,4.5)
# print(list1,list2)


# 浅拷贝：外层拷贝值，内层引用
# import copy
#
# list1 = [1,2,3,[4,5]]
# list2 = copy.copy(list1)
# print(list1 is list2)
# print(list1[1] is list2[1])
# list1.insert(3,3.5)
# print(list1,list2)
# list2[3].insert(1,4.5)
# print(list1,list2)


# 深拷贝：外层拷贝值，内层拷贝值
import copy

list1 = [1,2,3,[4,5]]
list2 = copy.deepcopy(list1)
print(list1 is list2)
print(list1[3] is list2[3])
list1.insert(3,3.5)
print(list1,list2)
list2[3].insert(1,4.5)
print(list1,list2)