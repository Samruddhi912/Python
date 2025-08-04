#Input:721
#Output: 1  2   7
def SumDigits(num):
    iSum=0
    while(num!=0):
        iDigit=num%10
        iSum=iDigit+iSum
        num=num//10
        
    return iSum

        
        

def main():
    print("Enter the number :")
    no=int(input())

    ans=SumDigits(no)
    print("Addition of digits is:",ans)
    
    
if __name__=="__main__":
    main()