def Display(no):
    for i in range(1,no+1):
        print("")
        for j in range(1,no+1):
            print(" ",j," ",end='')
def main():
    num=int(input("Enter one number: "))
    Display(num)

if __name__=="__main__":
    main()