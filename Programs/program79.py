'''     
$   $   $   $   $   $
  $   $   $   $   $ 
     $   $   $  
         $         
'''
def Display(iRow):
    for i in range(iRow,0,-1):
        print(" "*(iRow-i),end="")
        print("$ "*i)
            
def main():
    print("Enter Number of rows")
    Value1=int(input())
    
    Display(Value1)

if __name__=="__main__":
    main()