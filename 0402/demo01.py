'''
通过生成器节省内存
生成器特点：后续元素由前方元素确定
通过异常捕获 捕获生成器元素获取完毕
可以使用for循环或者next遍历生成器

'''
import  sys

list1 = [x for x in range(100000)]
print(sys.getsizeof(list1))
print(list1[100],type(list1))

list2 = (x for x in range(100000))
print(sys.getsizeof(list2))

list3 = (x for x in range(100))
print(sys.getsizeof(list3))

for i in list3:
    print(i,type(i))

while True:
    try:
        # print(next(list3))
        print(list3.__next__())
    except Exception as e:
        print(e)
        break