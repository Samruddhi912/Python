def ReverseArray(Brr):
    iStart=0
    iEnd=len(Brr)-1
    iTemp=0
    while(iStart<iEnd):
        iTemp=Brr[iStart]
        Brr[iStart]=Brr[iEnd]
        Brr[iEnd]=iTemp

        iStart+=1
        iEnd-=1

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ReverseArray(List)
    print(List)
    

if __name__=="__main__":
    main()