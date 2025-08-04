def Display(num):
    for i in range(num):
        print("*",end="\t");  
    
    print()
     
def main():
    print("Enter the number of * :")
    no=int(input())

    Display(no)
    
if __name__=="__main__":
    main()