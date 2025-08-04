def CountEvenOdd(Brr):
    iEven=0
    iOdd=0
    for i in Brr:
        if (i%2==0):
            iEven+=1
        else:
            iOdd+=1
    return iEven,iOdd

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ansEven,ansOdd=CountEvenOdd(List)
    print(f"Even and Odd number from List is:{ansEven} and {ansOdd}")

if __name__=="__main__":
    main()