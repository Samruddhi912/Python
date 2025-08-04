def ArrayReverse(Brr):
    Crr=[]
    for i in range(len(Brr)-1,-1,-1):
        Crr.append(Brr[i])
    return Crr

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ans=ArrayReverse(List)
    print("Reveresed array is:",ans)
    

if __name__=="__main__":
    main()