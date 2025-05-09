def Addition(num1,num2):
    ans=0
    ans=num1+num2
    return ans


def main():
    print("Enter two numbers: ")
    no1=int(input())
    no2=int(input())
    result=Addition(no1,no2)
    print("Addition is : ",result)

if __name__=="__main__":
    main()