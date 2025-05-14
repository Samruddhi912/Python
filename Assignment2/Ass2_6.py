def Display(no):
    for i in range(no):
        print("")
        for j in range(no-i):
            print("* ",end='')


def main():
    num=int(input("Enter one number: "))
    Display(num)

if __name__=="__main__":
    main()