def Display(iNo):
    for i in range(-iNo,iNo+1,1):
        print(i,end="")


def main():
    print("Enter NUMBER")
    num=input()
    Display(num)

if __name__=="__main__":
    main()