import sys
import os
import shutil
def DirectoryCopy(Dirname1,Dirname2):

    flag=os.path.isabs(Dirname1)
    if flag==False:
        Dirname1=os.path.abspath(Dirname1)

    flag=os.path.isabs(Dirname2)
    if flag==False:
        Dirname2=os.path.abspath(Dirname2)
    
    flag=os.path.exists(Dirname1)
    if flag==False:
        print("Path is invalid")
        exit()
    
    flag=os.path.isdir(Dirname1)
    if flag==False:
        print("Valid path but not directory")
        exit()
    
    if not os.path.exists(Dirname2):
        os.makedirs(Dirname2)
    
    filesCopied=0

    for Folder,SubFolders,Files in os.walk(Dirname1):
        for Fname in Files:
            SourceFile=os.path.join(Folder,Fname)

            RelativePath=os.path.relpath(Folder,os.path.abspath(Dirname1))
            DestFolder=os.path.join(os.path.abspath(Dirname2),RelativePath)
            #os.makedirs(Dirname2)
            DestFile=os.path.join(DestFolder,Fname)
            try:
                shutil.copy2(SourceFile,DestFile)
                filesCopied+=1
                print("Copied file name is:",Fname)
            except PermissionError:
                print(f"Permission denied:{Dirname1}")
    print("Total copied files are:",filesCopied)
            

def main():
    DName1=sys.argv[1]
    DName2=sys.argv[2]
    DirectoryCopy(DName1,DName2)
    

if __name__=="__main__":
    main()