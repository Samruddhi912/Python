import sys

def CompareContents(FFile,SFile):
    fobj1=open(FFile,"r")
    fobj2=open(SFile,"r")
    if fobj1.read()==fobj2.read():
        return True
    else:
        return False

def main():
    FirstFile=sys.argv[1]
    SecondFile=sys.argv[2]
    
    Res=CompareContents(FirstFile,SecondFile)
    if Res==True:
        print("Contents match")
    else:
        print("Contents do not match")

if __name__=="__main__":
    main()