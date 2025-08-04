def ReplaceLetter(Data):
    
    for ch in range(len(Data)):
        if(Data[ch]=="a"):
            Data[ch]="_" #error
        
def main():
    print("Enter String:")
    str=input()

    ReplaceLetter(str)

    print("Replaced letter in string is:",str)

if __name__=="__main__":
    main()