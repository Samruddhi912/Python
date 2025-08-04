def Addition(num1,num2):
    result=0; 
    result=num1+num2; 
    return result; 

def main():
    print("Enter two numbers: "); 
    no1=int(input()); 
    no2=int(input()); 
    ans=Addition(no1,no2); 

    print(f"Addition of {no1} & {no2} is : {ans}"); 

if __name__=="__main__":
    main()