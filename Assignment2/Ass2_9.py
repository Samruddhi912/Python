def Digits(no):
    count=0
    while(no!=0):
        
        count=count+1
        no=no//10
    return count
            
def main():
    num=int(input("Enter one number: "))
    ans=Digits(num)
    print(ans)

if __name__=="__main__":
    main()