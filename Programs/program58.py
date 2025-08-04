def CountSmall(Data):
    iCount=0
    for ch in Data:
        if(ch >="a" and ch<="z"):
            iCount+=1

    return iCount

def main():
    print("Enter String:")
    str=input()

    ans=CountSmall(str)

    print("Small letter in string is:",ans)

if __name__=="__main__":
    main()