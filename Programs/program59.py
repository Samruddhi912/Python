def ReplaceLetter(Data):
    Output=""
    for ch in Data:
        if(ch=="a"):
            Output.append("_") #Error
        else:
            Output.append(ch)
    return Output

def main():
    print("Enter String:")
    str=input()

    ans=ReplaceLetter(str)

    print("Replaced letter in string is:",ans)

if __name__=="__main__":
    main()