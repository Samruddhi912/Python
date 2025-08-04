def SumFact(num):
    iSum=0
    for i in range(1,(num//2)+1):
        if(num%i==0):
            iSum=iSum+i

    return iSum

def main():
    print("Enter the number :")
    no=int(input())

    ans=SumFact(no)
    print("Sum of factors is:",ans)

if __name__=="__main__":
    main()