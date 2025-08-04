def CountVowels(Data):
    iCount=0
    pattern="aeiouAEIOU"
    for ch in Data:
        if(ch in pattern):
            iCount+=1

    return iCount

def main():
    print("Enter String:")
    str=input()

    ans=CountVowels(str)

    print("Vowels in string is:",ans)

    
    
if __name__=="__main__":
    main()