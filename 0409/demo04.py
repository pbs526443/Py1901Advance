import threading,time

def myrun():
    print('++')
def thread1():
    print('--')

class MyThread(threading.Thread):
    def run(self):
        print('run')

def main():
    t = threading.Thread(target=thread1)
    print(t.run())
    t.run = myrun
    t.start()
    time.sleep(1)
    for i in range(5):
        t1 = MyThread()
        t1.start()
        time.sleep(1)

if __name__ == '__main__':
    main()