def MinNum(Brr):
    iMin=Brr[0]
    for i in Brr:
        if iMin>i:
            iMin=i
    return iMin

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ans=MinNum(List)
    print("Minimum number from List is:",ans)

if __name__=="__main__":
    main()