import threading
import os

def Small(StringCount):
    print("Id of Small is",os.getpid())
    print("Name of thread is",threading.current_thread())
    count=0
    for i in StringCount:
        if (i>='a' and i<='z'):
            count=count+1
    print("Number of small letters in string are:",count)

def Capital(StringCount):
    print("Id of Capital is",os.getpid())
    print("Name of thread is",threading.current_thread())
    count=0
    for i in StringCount:
        if (i>='A' and i<='Z'):
            count=count+1
    print("Number of Capital letters in string are:",count)

def NumberCount(num):
    print("Id of Number is",os.getpid())
    print("Name of thread is",threading.current_thread())
    count=0
    while(num>0):
        num%10
        count=count+1
        num/10
    print("Number of Digits",count)

def main():
    print("Enter string:")
    character=input()
    print("Enter number")
    no=int(input())
    T1=threading.Thread(target=Small,args=(character,))
    T1.start()
    T1.join()
    T2=threading.Thread(target=Capital,args=(character,))
    T2.start()
    T2.join()
    T3=threading.Thread(target=NumberCount,args=(no,))
    T3.start()
    T3.join()

if __name__=="__main__":
    main()