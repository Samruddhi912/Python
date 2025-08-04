def CountVowels(Data):
    iCount=0
    for ch in Data:
        if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
            iCount+=1

    return iCount

def main():
    print("Enter String:")
    str=input()

    ans=CountVowels(str)

    print("Vowels in string is:",ans)

    
    
if __name__=="__main__":
    main()