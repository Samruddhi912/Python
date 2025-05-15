def Add(List):
    sum=0
    for i in List:
        sum=sum+i
    return sum

def main():
    Data=[]
    print("Enter number of elements you want to enter:")
    num=int(input())
    print("Enter the elements:")
    for i in range(num):
        no=int(input())
        Data.append(no)
    Res=Add(Data)
    print("Addition of list is",Res)


if __name__=="__main__":
    main()

