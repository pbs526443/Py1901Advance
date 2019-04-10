from multiprocessing import Pool
from multiprocessing import Manager
import time
import re,requests

def timecount(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print('消耗时间为'+(end-start)+'s')
    return fun

def read():
    pass

def main():
    with open('1.txt','r') as f:
        s = f.read()
        result = re.findall(r'(.*?).jpg',s)
        print(result)
        for i in result:
            response = requests.get(i+'.jpg')
            content = response.content
            print(content)


if __name__ == '__main__':
    main()