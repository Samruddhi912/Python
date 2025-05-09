def ChkNum(num):
    if(num>=1):
        print("Number",num, "is Positive")
    elif(num==0):
        print("Number",num," is Zero")
    else:
        print("Number",num," is Negative")


def main():
    print("Enter one number: ")
    no=int(input())
    ChkNum(no)

if __name__=="__main__":
    main()