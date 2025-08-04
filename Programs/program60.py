def ReplaceLetter(Data):
    Output=""
    for ch in Data:
        if(ch=="a"):
            Output=Output+"_"
        else:
            Output=Output+ch
    return Output

def main():
    print("Enter String:")
    str=input()

    ans=ReplaceLetter(str)

    print("Replaced letter in string is:",ans)

if __name__=="__main__":
    main()