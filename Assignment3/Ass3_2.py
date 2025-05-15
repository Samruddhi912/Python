def ChkMax(List):
    Max=0
    for i in List:
        if Max<i:
            Max=i
    return Max


def main():
    Data=[]
    print("Enter number of elements:")
    num=int(input())
    print("Enter elements:")
    for i in range(num):
        no=int(input())
        Data.append(no)
    Res=ChkMax(Data)
    print("Maximum is",Res)

if __name__=="__main__":
    main()

