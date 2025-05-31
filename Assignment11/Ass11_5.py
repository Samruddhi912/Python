Count=0
def CountZero(Value1):
    global Count
    iDigit=0
    if(Value1>0):
        iDigit=Value1%10
        if(iDigit==0):
            Count=Count+1
        Value1=Value1//10
        CountZero(Value1)
    return Count
        
def main():
    no1=int(input("Enter number:"))
    Ans=CountZero(no1)
    print("Result:",Ans)


if __name__=="__main__":
    main()