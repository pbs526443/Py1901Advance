import threading,re,requests
import time

def fun(i,d):
    response = requests.get(i)
    content = response.content
    print(content)
    k = './img/%s.png' % d
    with open(k, 'wb') as f:
        f.write(content)

def timecount(f):
    '''20.84735417366028'''
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return  fun

@timecount
def main():
    d = 0
    with open('1.txt', 'r') as f:
        s = f.read()
        result = re.findall(r'(.*?)\n', s, re.S)
        theradlist = []
        for i in result:
            # d1 = re.split('/',i)[-1]
            t = threading.Thread(target=fun, args=(i, d))
            t.start()
            d = d + 1
            theradlist.append(t)
        for i in theradlist:
            i.join()

if __name__ == '__main__':
   main()