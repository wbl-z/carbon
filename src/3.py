import threading
import time
def a():
    print('a')
 
 
def b():
    print('b')
 
 
def c():
    while True:
        print('c')
        time.sleep(1)
 
 
if __name__ == '__main__':
    t = threading.Thread(target=c)
    t.setDaemon(True)
    t.start()
    while True:
        a()
        b()


