import sys
import shutil
def main():
    print(sys.argv[0])
    NewFile=sys.argv[1]
    fobj=(NewFile,"w")
    OldFile="demo.txt"
    shutil.copyfile(OldFile,NewFile)
    fobj=open(NewFile,"r")
    data=fobj.read()
    print("Contents from new",sys.argv[1] ,"file are:",data)


    

if __name__=="__main__":
    main()
