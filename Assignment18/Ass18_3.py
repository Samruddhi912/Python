import sys
import shutil
def Copy(SFile,DFile):
    sobj=open(SFile,"r")
    shutil.copyfile(SFile,DFile)
    dobj=open(DFile,"r")
    data=dobj.read()
    print("Contents in New File:",data)
    dobj.close()

def main():
    f1Name=sys.argv[1]
    f2Name=sys.argv[2]
    Copy(f1Name,f2Name)

if __name__=="__main__":
    main()
