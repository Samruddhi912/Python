import multiprocessing
import time
def Square(List):
    Result=[]
    for i in List:
        Ans=1
        Ans=i**2
        Result.append(Ans)
    print(Result)
def main():
    Start_time=time.time()
    Data=[]
    no=int(input("Enter number of element you want in list"))
    print("Enter numbers")
    for i in range(no):
        num=int(input())
        Data.append(num)
    Data2=[]
    no1=int(input("Enter number of element you want in list"))
    print("Enter numbers")
    for i in range(no1):
        num2=int(input())
        Data2.append(num2)
    p1=multiprocessing.Process(target=Square,args=(Data,))
    p1.start()
    p1.join()
    p2=multiprocessing.Process(target=Square,args=(Data2,))
    p2.start()
    p2.join()
    End_time=time.time()
    print("Time taken:",End_time-Start_time)

if __name__=="__main__":
    main()
