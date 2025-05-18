def ChkAge(Num):
    if(Num>=18):
        return True
    else:
        return False
    
def main():
    print("Enter a age")
    no=int(input())
    Res=ChkAge(no)
    if Res==True:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

if __name__=="__main__":
    main()