def ChkFrequency(FileWord,InputWord):
    obj=open(FileWord,"r")
    Count=obj.read().split().count(InputWord)

    obj.close()
    return Count



def main():
    print("Enter file name:")
    FName=input()
    fobj=open(FName,"w")
    fobj.write("Marvellous is good coding class. Marvellous is wonderfull")
    fobj.close()
    print("Enter String to check frequency of a word in the file")
    Frequency=input()
    Res=ChkFrequency(FName,Frequency)
    print("Frequency of the word is:",Res)

if __name__=="__main__":
    main()