from functools import reduce

def Prime(Num):
    for i in range(2,Num):
        if(Num%i==0):
            return False
    return Num
    
def Mult(Num):
    return Num*2

def Max(Num1,Num2):
    if(Num1>Num2):
        return Num1
    return Num2
        
def main():
    Data=[]
    no=int(input("Enter number of elements"))
    print("Enter elements")
    for i in range(no):
        num=int(input())
        Data.append(num)
    print(Data)
    fData=list(filter(Prime,Data))
    print(fData)
    mData=list(map(Mult,fData))
    print(mData)
    rData=reduce(Max,mData)
    print(rData)



if __name__=="__main__":
    main()