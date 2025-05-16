def Display(no):
    for i in range(no):
        print("")
        for j in range(i+1):
            print(" * ",end='')
    print("") 

def main():
    print("Enter a num")
    num=int(input())
    Display(num)


if __name__=="__main__":
    main()