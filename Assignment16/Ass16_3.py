def ChkCount(FileName):
    fobj=open(FileName,"r")
    LineCount=0
    WordCount=0
    ChracterCount=0
    for line in fobj:
        LineCount=LineCount+1
        words=line.split()
        WordCount+=len(words)
        ChracterCount+=len(line)
    return LineCount,WordCount,ChracterCount


def main():
    print("Enter file name:")
    FName=input()
    Res=ChkCount(FName)
    print("Number of Lines,Number of Words,Number of characters:",Res)
    



if __name__=="__main__":
    main()