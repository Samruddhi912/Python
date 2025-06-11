import shutil
def CopyContents(SFIle,DFile):
    sobj=open(SFIle,"r")
    shutil.copyfile(SFIle,DFile)
    dobj=open(DFile,"r")
    data=dobj.read()
    print(data)
    sobj.close()
    dobj.close()


def main():
    print("Enter source file name:")
    SourceFile=input()
    print("Enter destination file name:")
    DestinationFile=input()
    fobj=open(SourceFile,"w")
    fobj.write("My name is Samruddhi Kadam.\nI am 21 year old\nI am currently pursuing B.tech degree from PVG College,Pune\nI love coding\nMy hobbies are swimming,reading,dancing")
    fobj.close()
    CopyContents(SourceFile,DestinationFile)


if __name__=="__main__":
    main()