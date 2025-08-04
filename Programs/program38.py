def Addition(Brr):
    iSum=0
    for i in Brr:
        iSum=iSum+i
    return iSum

def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    ans=Addition(List)
    print("Addition of List is:",ans)

if __name__=="__main__":
    main()