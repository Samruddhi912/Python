def Update(Brr):
    for i in range(len(Brr)-1,-1,-1):
        if(Brr[i]%2==0):
            Brr[i]=Brr[i]+1
    
def main():
    List=[]
    print("Enter number of elements:")
    iSize=int(input())
    print("Enter the elements:")
    for i in range(iSize):
        elements=int(input())
        List.append(elements)
    Update(List)
    print(List)
    

if __name__=="__main__":
    main()