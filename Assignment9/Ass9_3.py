import multiprocessing

def Fact(factNo):
    Factnum=1
    for i in range(1,factNo+1):
        Factnum=Factnum*i
    print(f"Factorial of {factNo} is {Factnum}")

def main():
    Data=[]
    no=int(input("Enter number of elements you want to enter"))
    print("Enter Elements")
    for i in range(no):
        num=int(input())
        Data.append(num)
    p1=multiprocessing.Pool()
    p1.map(Fact,Data)
    

if __name__=="__main__":
    main()
            