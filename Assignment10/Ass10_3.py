from functools import reduce

def Greater(Number):
    if(Number>=70 and Number<=90):
        return Number

def Increase(Number):
    return Number+10


def Product(Num1,Num2):
    return Num1*Num2

def main():
    Data=[]
    no=int(input("Enter number of elements"))
    print("Enter elements")
    for i in range(no):
        num=int(input())
        Data.append(num)
    print(Data)
    fData=list(filter(Greater,Data))
    print(fData)
    mData=list(map(Increase,fData))
    print(mData)
    rData=(reduce(Product,mData))
    print(rData)

if __name__=="__main__":
    main()