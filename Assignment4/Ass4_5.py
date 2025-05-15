from functools import reduce
def ChkPrime(Number):
    for i in range(2,Number):
        if(Number%i==0):
            return False
    return Number

Mult=lambda Number: Number*2

def ChkMax(Num1,Num2):
    if Num1>Num2:
        return Num1
    else:
        return Num2
    


def main():
    Data=[]
    print("Enter the number of elements")
    num=int(input())
    print("Enter the elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("List is ",Data)

    fData=list(filter(ChkPrime,Data))
    print("Filtered Data is",fData)
    mData=list(map(Mult,fData))
    print("Mapped Data is",mData)
    rdata=reduce(ChkMax,mData)
    print("Reduced Data is",rdata)


if __name__=="__main__":
    main()
