def SumNum(num):
    iCount=0
    for i in range(1,num+1):
        iCount=iCount+i
    return iCount

def main():
    print("Enter the number :")
    no=int(input())

    ans=SumNum(no)
    print(f"Sum of digits of {no} is : {ans}"); 
    
if __name__=="__main__":
    main()