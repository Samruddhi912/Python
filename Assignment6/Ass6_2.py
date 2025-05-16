def AddEven():
    num=1
    sum=0
    while num<=100:
        if(num%2==0):
            sum=sum+num
        num+=1
    return sum

def main():
    Res=AddEven()
    print("Sum of even nymber from 1 to 100",Res)
if __name__=="__main__":
    main()