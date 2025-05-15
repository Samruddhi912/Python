from functools import reduce
ChkEven=lambda Number:Number%2==0

ChkSquare=lambda Number: Number**2

ChkAdd=lambda Num1,Num2:Num1+Num2


def main():
    Data=[]
    print("Enter the number of elements")
    num=int(input())
    print("Enter the elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("List is ",Data)
    fData=list(filter(ChkEven,Data))
    print("Filtered Data is",fData)
    mData=list(map(ChkSquare,fData))
    print("Mapped Data is",mData)
    rdata=reduce(ChkAdd,mData)
    print("Reduced Data is",rdata)


if __name__=="__main__":
    main()
