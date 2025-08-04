def ChkEvenOdd(no):
    if ((no%2)==0):
        return True; 
    else:
        return False; 

def main():
    print("Enter number"); 
    no1=int(input()); 
    ans=ChkEvenOdd(no1)
    if (ans==True):
        print(f"{no1} is Even number"); 
    else:
        print(f"{no1} is Odd Number"); 


if __name__=="__main__":
    main()