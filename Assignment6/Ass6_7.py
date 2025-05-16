def ChkMax(A):
    iMax=A[0]
    for i in A:
        if(iMax<i):
            iMax=i
    return iMax
    



def main():
    Data=[]
    print("Enter 5 numbers")
    for i in range(5):
        num=int(input())
        Data.append(num)
    Res=ChkMax(Data)
    print(Res)

        

if __name__=="__main__":
    main()