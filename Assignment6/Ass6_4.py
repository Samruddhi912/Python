def Fact(no):
    Product=1
    for i in range(1,no+1):
        Product=Product*i
    return Product


def main():
    print("Enter number")
    num=int(input())
    Res=Fact(num)
    print("Factorial of",num,"is",Res)

if __name__=="__main__":
    main()