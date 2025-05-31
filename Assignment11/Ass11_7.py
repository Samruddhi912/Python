i=1
j=1
def Display(Num1):
    global i
    if(i<=Num1):
        global j
        if(j<=i):
            print("*",end=' ')
            j=j+1
        print()
        i=i+1
        Display(i)

def main():
    no1=int(input("Enter number:"))

    Display(no1)
    


if __name__=="__main__":
    main()