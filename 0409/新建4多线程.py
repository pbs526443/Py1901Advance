import threading,re,requests

def fun(i,d):
    response = requests.get(i)
    content = response.content
    print(content)
    k = './img/%s.png' % d
    with open(k, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    d = 0
    with open('1.txt','r') as f:
        s = f.read()
        result = re.findall(r'(.*?)\n', s, re.S)
        for i in result:
            t = threading.Thread(target=fun,args=(i,d))
            t.start()
            d = d+1