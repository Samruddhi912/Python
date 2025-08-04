'''
         $              3
     $   $   $          2
  $   $   $   $   $     1
$   $   $   $   $   $   0
  $   $   $   $   $     1
     $   $   $          2
         $              3
'''
def Display(iRow):
    for i in range(1,iRow+1):
        print(" "*(iRow-i),end="")
        print("$ "*i)
    for i in range(iRow,0,-1):
        print(" "*(iRow-i),end="")
        print("$ "*i)
      
def main():
    print("Enter Number of rows")
    Value1=int(input())
    
    Display(Value1)

if __name__=="__main__":
    main()