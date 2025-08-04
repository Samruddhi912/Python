def ConvertUpper(Data):
    output=""
    for ch in range(len(Data)):
        if(Data[ch]>="a" and Data[ch]<="z"):
            output=output+chr(ord(Data[ch])-32)  
        else:
            output=output+Data[ch]

    return output
        
        
def main():
    print("Enter String:")
    str=input()

    ans=ConvertUpper(str)

    print("Updated string is:",ans)

if __name__=="__main__":
    main()