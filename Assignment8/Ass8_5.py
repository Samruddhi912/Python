import threading
def Forward():
    print("Forward Printing")
    for i in range(1,51):
        
        print(i)
def Reverse():
    print("Reverse Printing")
    for i in range(50,0,-1):
        print(i)

def main():
    t1=threading.Thread(target=Forward)
    t1.start()
    t1.join()
    t2=threading.Thread(target=Reverse)
    t2.start()
    
    t2.join()

if __name__=="__main__":
    main()