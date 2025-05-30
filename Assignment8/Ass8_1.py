import threading
def Even():
    print("Display Even Numbers")
    for i in range(2,20,2):
        print(i)

def Odd():
    print("Display Odd Numbers")
    for i in range(1,20,2):
        print(i)


def main():
    T1=threading.Thread(target=Even)
    T2=threading.Thread(target=Odd)
    T1.start()
    T2.start()
    T1.join()
    T2.join()


if __name__=="__main__":
    main()
