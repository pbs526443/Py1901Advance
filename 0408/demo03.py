from multiprocessing import Process

def processmain(pam1,pam2,**kwargs):
    print('++',pam1[0],pam2,kwargs)
    print(kwargs['name'])

def main():
    list1 = [1]
    p1 = Process(target=processmain,args=(list1,list1),kwargs={'name':'pbs'})
    p1.start()

if __name__ == "__main__":
    main()