def Display(num):
    i=1; 
    while(i<=num):
        print("*",end="\t"); 
        i=i+1;  
    
    print()
     
def main():
    print("Enter the number of * :")
    no=int(input())

    Display(no)
    
if __name__=="__main__":
    main()