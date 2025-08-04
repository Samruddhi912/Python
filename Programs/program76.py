'''
$   $   $   $   $
$   $   $   $   $
$   $   $   $   $
$   $   $   $   $
$   $   $   $   $
'''
def Display(iRow,iCol):
    for i in range(1,iRow+1):
        print("$\t"*iCol)
            
def main():
    print("Enter Number of rows")
    Value1=int(input())
    print("Enter Number of Columns")
    Value2=int(input())
    Display(Value1,Value2)

if __name__=="__main__":
    main()