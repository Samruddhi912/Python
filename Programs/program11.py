
def Division(num1,num2):
    ans=0; 
    if(num2==0):
        print("Enter non-zero numbers"); 
        exit(); 
    else:
        ans=num1//num2 #floorDivision->downgrade 
        return ans
    

def main():
    print("Enter two numbers")
    no1=int(input())
    no2=int(input())
    

    ans=Division(no1,no2)
    print(f"Division of {no1} and {no2} is : {ans}")

if __name__=="__main__":
    main()