def ChkPerfect(num):
    iSum=0
    for i in range(1,(num//2)+1):
        if(num%i==0):
            iSum=iSum+i
    
    if(iSum==num):
        return True
    else:
        return False
    
def main():
    print("Enter the number :")
    no=int(input())

    ans=ChkPerfect(no)
    if ans==True:
        print("Number is Perfect Number")
    else:
        print("Number is not a Perfect Number")

if __name__=="__main__":
    main()