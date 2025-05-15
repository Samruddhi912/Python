def Frequency(List,Number):
    Count=0
    iPos=Number
    for i in List:
        if iPos==i:
            Count+=1
    return Count



def main():
    Data=[]
    print("Enter number of elements:")
    num=int(input())
    print("Enter elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    FindNo=int(input("Number you want to search: "))
    Res=Frequency(Data,FindNo)
    print("The Frequency of number is :",Res)

if __name__=="__main__":
    main()
