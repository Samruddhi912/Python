def Display(num):
    for i in range(num,0,-1):
        print(i,end="\t")

    for i in range(2,num+1,1):
        print(i,end="\t")


def main():
    print("Enter value")
    num1=int(input())
    Display(num1)

if __name__=="__main__":
    main()