def ReverseNum(num):
    iDigit=0
    iRev=0
    while(num!=0):
        iDigit=num%10
        iRev=iRev*10+iDigit
        num=num//10
    
    return iRev

def main():
    print("Enter the number :")
    no=int(input())

    ans=ReverseNum(no)
    print(f"Reverse Number of {no} is : {ans}")
 
    
if __name__=="__main__":
    main()