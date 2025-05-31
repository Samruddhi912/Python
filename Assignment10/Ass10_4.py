from functools import reduce

def Even(Num):
    if(Num%2==0):
        return Num

def Square(Num):
    return Num**2

def Add(Num1,Num2):
    return Num1+Num2

def main():
    Data=[]
    no=int(input("Enter number of elements"))
    print("Enter elements")
    for i in range(no):
        num=int(input())
        Data.append(num)
    print(Data)
    fData=list(filter(Even,Data))
    print(fData)
    mData=list(map(Square,fData))
    print(mData)
    rData=reduce(Add,mData)
    print(rData)



if __name__=="__main__":
    main()