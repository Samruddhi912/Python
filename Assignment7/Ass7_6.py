def ChkPrime(PrimeNum):
    for i in range(2,PrimeNum):
        if(PrimeNum%i==0):
            return False
        else:
            return PrimeNum
def main():
    Data=[]
    print("Number of elements you want to enter")
    num=int(input())
    print("Enter elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("Original List:",Data)
    
    fData=list(filter(ChkPrime,Data))
    print(fData)
if __name__=="__main__":
    main()
