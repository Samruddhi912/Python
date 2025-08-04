def ChkDivisible(num):
    if ((num%3==0) and (num%5==0)):
        return True
    else:
        return False

def main():
    print("Enter number")
    no1=int(input())
    ans=ChkDivisible(no1)
    if ans==True:
        print(f"{no1} is Divisibe by 3 & 5")
    else:
        print(f"{no1} is not divisible by 3 or 5")

if __name__=="__main__":
    main()