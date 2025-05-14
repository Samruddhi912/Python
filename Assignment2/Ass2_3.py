def Fact(no):
    sum=1
    for i in range(1,no+1):
        sum=sum*i
    return sum


def main():
    print("Enter one number:")
    num=int(input())
    Result=Fact(num)
    print(Result)

if __name__=="__main__":
    main()