Res=0
def Add(Value1):
    global Res
    if(Value1>0):
        Res=Res+Value1
        Value1=Value1-1
        Add(Value1)
    return Res
        
def main():
    no1=int(input("Enter number:"))
    Ans=Add(no1)
    print("Result:",Ans)


if __name__=="__main__":
    main()