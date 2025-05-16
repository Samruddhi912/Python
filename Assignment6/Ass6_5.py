def Prime(no):
    Ans=1
    for i in range(2,no):
        if(no%i==0):
            return False
    return True


def main():
    print("Enter number")
    num=int(input())
    Res=Prime(num)
    if Res==True:
        print(num,"is a Prime num")
    else:
        print(num,"is not a Prime num")


if __name__=="__main__":
    main()