import threading
import time
def no():
    for i in range(1,6):
        time.sleep(1)
        print(i)

def main():
    t1=threading.Thread(target=no)
    t2=threading.Thread(target=no)
    t3=threading.Thread(target=no)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()

if __name__=="__main__":
    main()
