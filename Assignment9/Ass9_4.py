import time
import threading
import multiprocessing
def Add(num):
    Ans=0
    for i in range(1,num+1):
        Ans=Ans+i
    print("Result ",Ans)

def main():
    S1_time=time.time()
    Add(1000000000)
    E1_time=time.time()
    print("time for normal function to execute:",E1_time-S1_time)
    S2_time=time.time()
    t1=threading.Thread(target=Add,args=(1000000000,))
    t1.start()
    t1.join()
    E2_time=time.time()
    print("time for Threading function to execute:",E2_time-S2_time)
    S3_time=time.time()
    p1=multiprocessing.Process(target=Add,args=(1000000000,))
    p1.start()
    p1.join()
    E3_time=time.time()
    print("time for Threading function to execute:",E3_time-S3_time)

if __name__=="__main__":
    main()