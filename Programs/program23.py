def CountEvenDigits(num):
    iCount=0
    iDigit=0
    while(num!=0):
        iDigit=num%10
        if(iDigit%2==0):
            iCount=iCount+1
        num=num//10
        
    return iCount

def main():
    print("Enter the number :")
    no=int(input())

    ans=CountEvenDigits(no)
    print(f"Number of even digits in {no} is:{ans}")
 
    
if __name__=="__main__":
    main()