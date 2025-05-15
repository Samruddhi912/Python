from MarvellousNum import ChkPrime
def ListPrime(List):
    sum=0
    for i in List:
        sum=sum+i
    return sum

def main():
    Data=[]
    print("Enter number of elements:")
    num=int(input())
    print("Enter Elements:")
    for i in range(num):
        no=int(input())
        if ChkPrime(no)==True:
            Data.append(no)

        
    
    Answer=ListPrime(Data)
    print("Addition of Prime number in List is:",Answer)
    
if __name__=="__main__":
    main()