import threading
import os
import time
l1 = ["asdf","asd","ytg","sd"]
def input_take():
    l2=[12,23,4,7,2,"23"]
    while True:
        if(len(l2)==0 ):
            break
        l1.append(l2[0])
        l2.remove(l2[0])
    return
def print_queue():
    while True:
        time.sleep(1)
        print(l1[0])
        l1.remove(l1[0])
        if(len(l1)==0 ):
            break
    return
t1 = threading.Thread(target=input_take)
t2 = threading.Thread(target=print_queue)


t1.start()
t2.start()
t2.join()
t1.join()



    
