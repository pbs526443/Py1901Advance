
# = 相当于引用

list1 =[1,2,3]
list2 = list1

print(list1 is list2)
list1.append(4)
print(list1,list2)
print(list1 is list2)


# 浅拷贝：外层拷贝值，内层引用
import copy
list3 = [1,2,3,[4,5]]
list4 = copy.copy(list3)
print(list3,list4)
print(list4 is list3)
print(list3[1] is list4[1])
print(list3[3] is list4[3])
list3.insert(3,3.5)
print(list3,list4)
list4[3].insert(1,4.5)
print(list3,list4)


# 深拷贝：外层拷贝值，内层也拷贝值
list5 = [1,2,3,[4,5]]
list6 = copy.deepcopy(list5)
print(list5,list6,list5 is list6)

list5.insert(3,3.5)
print(list5,list6)
print(list5[4] is list6[3])

list6[3].insert(1,4.5)
print(list5,list6)
