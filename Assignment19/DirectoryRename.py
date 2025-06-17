import sys
import os
from pathlib import Path

def DirectoryRename(DirName,ExName1,ExName2):
    flag=os.path.isabs(DirName)
    if flag==False:
        DirName=os.path.abspath(DirName)
    
    flag=os.path.exists(DirName)
    if flag==False:
        print("Path is invalid")
        exit()
    
    flag=os.path.isdir(DirName)
    if flag==False:
        print("Valid path but not directory")
        exit()
    
    for Folder,SubFolders,Files in os.walk(DirName):
        for fName in Files:
            if fName.endswith(ExName1):
                OldPath=os.path.join(Folder,fName)
                OldPath=Path(OldPath)
                NewPath=OldPath.with_suffix(ExName2)
                OldPath.rename(NewPath)
                print("Renamed files is:",NewPath)


def main():
    DName=sys.argv[1]
    Extension1=sys.argv[2]
    Extension2=sys.argv[3]
    DirectoryRename(DName,Extension1,Extension2)


if __name__=="__main__":
    main()