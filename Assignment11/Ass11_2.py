Fact=1
def Display(Value):
    global Fact
    if(Value>=1):
        Fact=Fact*Value
        Value=Value-1
        Display(Value)
    return Fact


    

def main():
    no=int(input("Enter number:"))
    Ans=Display(no)
    print(Ans)


if __name__=="__main__":
    main()