def NumOccurance(num):
    iCount4=0
    iCount5=0
    iCount7=0

    iDigits=0
    while(num!=0): 
        iDigits=num%10
        if(iDigits==5):
            iCount5=iCount5+1
        elif(iDigits==4):
            iCount4+=1
        elif(iDigits==7):
            iCount7+=1

        num=num//10
    return iCount4,iCount5,iCount7
            
def main():
    print("Enter the number :")
    no=int(input())

    ans4,ans5,ans7=NumOccurance(no)
    print(f"Occurance of 4,5,7 in {no} is : {ans4} , {ans5} , {ans7}")
 
    
if __name__=="__main__":
    main()