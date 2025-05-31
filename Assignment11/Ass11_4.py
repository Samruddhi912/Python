Ans=1
def Power(Value1,Value2):
    global Ans
    if(Value2>0):
        Ans=Ans*Value1
        Value2=Value2-1
        Power(Value1,Value2)

    return Ans
        
def main():
    no1=int(input("Enter number:"))
    no2=int(input("Enter number:"))
    Ans=Power(no1,no2)
    print("Result:",Ans)


if __name__=="__main__":
    main()