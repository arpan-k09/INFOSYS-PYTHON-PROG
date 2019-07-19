from threading import Thread #threading module should be imported
def tryit1():
    name=input("Enter your name")
    print("Hi your name is ",name)

def tryit2():
    for i in range(1,1000):
        x=i*2.0
    print("Done")

thread1=Thread(target=tryit1)   #we are creating one thread for tryit1
thread1.start()     #we are starting that thread
thread2=Thread(target=tryit2)   #we are creating one thread for tryit2
thread2.start()     #we are starting that thread
#we are waiting for the threads to complete using join.
thread1.join()
thread2.join()