def Table(no):
    Digit=1
    Product=1
    while(Digit<=10):
        Product=no*Digit
        print(no,"*",Digit,"=",Product)
        Digit+=1
    
def main():
    print("Enter number")
    num=int(input())
    Table(num)
    

if __name__=="__main__":
    main()