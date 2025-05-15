from functools import reduce
def Filtering(Number):
    if((Number>=70)&(Number<=90)):
        return Number
    
def Increase(Number):
    return Number+10

def Product(Num1,Num2):
    return Num1*Num2

def main():
    Data=[]
    print("Enter number of elements")
    num=int(input())
    print("Enter Elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("List is ",Data)
    fData=list(filter(Filtering,Data))
    print("Filtered Data:",fData)
    mData=list(map(Increase,fData))
    print("Mapped Data is ",mData)
    rData=reduce(Product,mData)
    print("Reduced value is ",rData)

if __name__=="__main__":
    main()
    