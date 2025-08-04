def NumOccurance(num):
    iCount=0
    iDigits=0
    while(num!=0):
        iDigits=num%10
        for i in range(1,num+1):
            if(iDigits==i):
                iCount=iCount+1
                print(iCount)
        num=num//10
    return iCount

def main():
    print("Enter the number :")
    no=int(input())

    ans=NumOccurance(no)
    print(f"Reverse Number of {no} is : {ans}")
 
    
if __name__=="__main__":
    main()