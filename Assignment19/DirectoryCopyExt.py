import sys
import os
import shutil
def DirectoryCopyExt(FName1,FName2,Ext):
    flag=os.path.isabs(FName1)
    if not FName1==flag:
        FName1=os.path.abspath(FName1)
    
    flag=os.path.isabs(FName2)
    if not FName2==flag:
        FName2=os.path.abspath(FName2)
    
    flag=os.path.exists(FName1)
    if flag==False:
        print("Invalid Path")
        exit()
    
    flag=os.path.exists(FName2)
    if flag==False:
        print("Invalid Path")
        exit

    flag=os.path.isdir(FName1)
    if flag==False:
        print("Valid path but not a directory")
        exit()

    flag=os.path.isdir(FName2)
    if flag==False:
        os.makedirs(FName2)

    for Folder,SubFolders,Files in os.walk(FName1):
        for Fnames in Files:
            Sourcefile=os.path.join(Folder,Fnames)

            RelativePath=os.path.relpath(Folder,os.path.abspath(FName1))
            DestFolder=os.path.join(os.path.abspath(FName2),RelativePath)
            
            DestFile=os.path.join(DestFolder,Fnames)
            try:
                if(Sourcefile.endswith(Ext)):
                    shutil.copy2(Sourcefile,DestFile)
            except PermissionError:
                print(f"Permission denied : {Sourcefile}")


def main():
    fileName1=sys.argv[1]
    fileName2=sys.argv[2]
    fileExt=sys.argv[3]
    if not sys.argv[3]:
        print("SourceFolder  DestinantionFolder  ExtensionName")
    DirectoryCopyExt(fileName1,fileName2,fileExt)


if __name__=="__main__":
    main()