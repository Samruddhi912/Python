def Display(no):
    for i in range(no):
        print("")
        for j in range(no):
            print(" * ",end='')

def main():
    print("Enter one number :")
    num1=int(input())
    Display(num1)


if __name__=="__main__":
    main()