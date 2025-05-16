Double=lambda A:A*2
def main():
    Data=[]
    print("Number of elements you want to enter")
    num=int(input())
    print("Enter elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("Original List:",Data)
    
    mData=list(map(Double,Data))
    print(mData)
if __name__=="__main__":
    main()
