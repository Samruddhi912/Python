import os
import sys

def DirectorySearch(FName,ExName):
    flag=os.path.isabs(FName)
    if flag==False:
        flag=os.path.abspath(FName)

    flag=os.path.exists(FName)
    if flag==False:
        print("Invalid path")
        exit()

    flag=os.path.isdir(FName)
    if flag==False:
        print("Valid path but incorrect directory")
        exit()
    
    for Folder,SubFolders,Files in os.walk(FName):
        for Fname in Files:
            if Fname.endswith(ExName):
                print(Fname)



def main():
    FileName=sys.argv[1]
    Extension=sys.argv[2]
    DirectorySearch(FileName,Extension)

if __name__=="__main__":
    main()
