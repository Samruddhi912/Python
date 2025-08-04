def MaxNum(Brr):
    iMax=Brr[0]
    for i in Brr:
        if iMax<i:
            iMax=i
    return iMax

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ans=MaxNum(List)
    print("Maximum number from List is:",ans)

if __name__=="__main__":
    main()