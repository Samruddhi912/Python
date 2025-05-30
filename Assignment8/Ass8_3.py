import threading
def EvenList(ListEven):
    Add=0
    for i in ListEven:
        Add=Add+i
    print("Addition of Even number List:",Add)

def OddList(ListOdd):
    Add=0
    for i in ListOdd:
        Add=Add+i
    print("Addition of Odd number List:",Add)

def main():
    Data=[]
    print("enter number of elements you want to enter")
    no=int(input())
    print("Enter Even Elements")
    for i in range (no):
        num=int(input())
        Data.append(num)
    Data2=[]
    print("enter number of elements you want to enter")
    no2=int(input())
    print("Enter Even Elements")
    for i in range (no2):
        num2=int(input())
        Data2.append(num2)
    T1=threading.Thread(target=EvenList,args=(Data,))
    T2=threading.Thread(target=OddList,args=(Data2,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__=="__main__":
    main()
