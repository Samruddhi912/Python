def CountOccurrance(Data):
    iCount=0
    for ch in Data:
        if(ch=="a"):
            iCount+=1

    return iCount

def main():
    print("Enter String:")
    str=input()

    ans=CountOccurrance(str)

    print("Occurance of 'a' in string is:",ans)

    
    
if __name__=="__main__":
    main()