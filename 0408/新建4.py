from multiprocessing import Process
import os

def p1process(pam1,pam2,**kwargs):
    print(pam1[0],pam2[0],kwargs['name'])
    pam1[0] = 12
    print(pam1[0])


def main():
    list1 = [1]
    list2 = [2]
    p1 = Process(target=p1process, args=(list1, list2), kwargs={'name': 'qwe'})
    p1.start()
    print(list1)

if __name__ == '__main__':
    main()