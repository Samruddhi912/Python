def NumOccurance(num):
    iCount=0
    iDigits=0
    while(num!=0): 
        iDigits=num%10
        if(iDigits==5):
            iCount=iCount+1
        num=num//10
    return iCount
            
def main():
    print("Enter the number :")
    no=int(input())

    ans=NumOccurance(no)
    print(f"Occurance of 5 in {no} is : {ans}")
 
    
if __name__=="__main__":
    main()