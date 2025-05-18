def ChkEven(Num):
    if(Num%2==0):
        return True
    else:
        return False
    
def main():
    print("Enter a number")
    no=int(input())
    Res=ChkEven(no)
    if Res==True:
        print(no,"Number is Even")
    else:
        print(no,"Number is Odd")

if __name__=="__main__":
    main()