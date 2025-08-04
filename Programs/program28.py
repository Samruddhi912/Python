def DisplayFact(num):
    print(f"Factors of {num} are :")
    for i in range(1,num):
        if(num%i==0):
            print(i)

def main():
    print("Enter the number :")
    no=int(input())

    DisplayFact(no)

if __name__=="__main__":
    main()