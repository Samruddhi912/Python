def ChkDiv(num):
    if((num%5)==0):
        return True
    else:
        return False


def main():
    print("Enter one number")
    no=int(input())
    Result=ChkDiv(no)
    print(Result)

if __name__=="__main__":
    main()