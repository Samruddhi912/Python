def ChkMin(List):
    Min=List[0]
    for i in List:
        if Min>i:
            Min=i
    return Min


def main():
    Data=[]
    print("Enter number of elements:")
    num=int(input())
    print("Enter elements:")
    for i in range(num):
        no=int(input())
        Data.append(no)
    Res=ChkMin(Data)
    print("Minimum is",Res)

if __name__=="__main__":
    main()

