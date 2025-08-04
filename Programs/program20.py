def FactNum(num):
    iFact=1
    for i in range(1,num+1):
        iFact=iFact*i
    return iFact

def main():
    print("Enter the number :")
    no=int(input())

    ans=FactNum(no)
    print(f"Sum of digits of {no} is : {ans}"); 
    
if __name__=="__main__":
    main()