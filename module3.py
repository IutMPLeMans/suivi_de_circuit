import threading
import time
def hello():
    print('go')
t=threading.Timer(5.0, hello)
t.start() 
 
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
 
 
#Autre version
import threading
import time
def timer(s):
    for i in range(s,0,-1):
        print(i)
        time.sleep(1)
 
t=threading.Thread(target=timer, args=[5])
t.start()
t.join()
print('start game')
