#Input:721
#Output: 1  2   7
def DisplayDigits(num):
    while(num!=0):
        iDigit=num%10
        num=num//10
        print(iDigit)

        
        

def main():
    print("Enter the number :")
    no=int(input())

    DisplayDigits(no)
    
    
if __name__=="__main__":
    main()