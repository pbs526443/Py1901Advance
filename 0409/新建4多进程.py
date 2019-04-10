from multiprocessing import Pool
import requests,re,time


def write(i,d):
    response = requests.get(i)
    content = response.content
    print(content)
    k = './img/%s.png' % d
    with open(k, 'wb') as f:
        f.write(content)

def timecount(f):
    ''' 21.395724296569824 '''
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return  fun

@timecount
def main():
    pool = Pool(4)
    d = 0
    with open('1.txt','r') as f:
        s = f.read()
        result = re.findall(r'(.*?)\n',s, re.S)
        # print(result)
        d = 0
        for i in result:
            pool.apply_async(write,(i,d))
            d = d + 1
        pool.close()
        pool.join()
if __name__ == '__main__':
    main()