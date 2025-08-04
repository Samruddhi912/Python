'''
$   
*   $  
*   *   $   
*   *   *   $

'''
def Display(iRow,iCol):
    if(iRow!=iCol):
        print("Invalid Pattern")
        return
    for i in range(1,iRow+1):
        for j in range(1,iCol+1):
            if (i==j):
                print("$",end="\t")
            elif(i>j):
                print("*",end="\t")
            
        print()

def main():
    print("Enter Number of rows")
    Value1=int(input())
    print("Enter Number of Columns")
    Value2=int(input())
    Display(Value1,Value2)

if __name__=="__main__":
    main()