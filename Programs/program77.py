'''     
            $      
        $   $   $ 
    $   $   $   $   $  
$   $   $   $   $   $   $
'''
def Display(iRow):
    for i in range(1,iRow+1):
        print("$\t"*i)
            
def main():
    print("Enter Number of rows")
    Value1=int(input())
    
    Display(Value1)

if __name__=="__main__":
    main()