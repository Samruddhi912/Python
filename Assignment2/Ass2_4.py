def Factors(no):
    sum=0
    for i in range(1,no):
        if(no%i==0):
            sum=sum+i
    return sum

def main():
    num=int(input("Enter one number :"))
    ans=Factors(num)
    print("Sum of factors is",ans)
   



if __name__=="__main__":
    main()