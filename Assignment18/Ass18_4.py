import sys

def Compare(SFile,DFile):
    sobj=open(SFile,"r")
    dobj=open(DFile,"r")
    if sobj.read().split()==dobj.read().split():
        return True
    else:
        return False

def main():
    f1Name=sys.argv[1]
    f2Name=sys.argv[2]
    Res=Compare(f1Name,f2Name)
    if Res==True:
        print("Contents in both files are same")
    else:
        print("Contents in both files are not same")

if __name__=="__main__":
    main()
