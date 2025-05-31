Sum=0
def Display(Value):
    global Sum
    iDigit=0
    if(Value>0):
        iDigit=Value%10
        Sum=Sum+iDigit
        Value=Value//10
        Display(Value)
    return Sum

def main():
    no=int(input("Enter number:"))
    Ans=Display(no)
    print(Ans)


if __name__=="__main__":
    main()