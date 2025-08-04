def ArrayReverse(Brr):
    for i in range(len(Brr)-1,-1,-1):
        print(Brr[i])

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ArrayReverse(List)
    

if __name__=="__main__":
    main()