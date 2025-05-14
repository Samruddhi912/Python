def ChkPrime(no):
    for i in range(2,no):
        if(no%i==0):
            return True
        else:
            return False

def main():
    print("Enter number:")
    num=int(input())
    ans=ChkPrime(num)
    if (ans==True):
        print("It is not prime number")
    else:
        print("It is a prime number")


if __name__=="__main__":
    main()