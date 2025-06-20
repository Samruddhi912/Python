import sys
import os
import hashlib

def CheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()
    buffer=fobj.read(BlockSize)
    while (len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def DirectoryCheckSum(DName):
    flag=os.path.isabs(DName)
    if flag==False:
        DName=os.path.abspath(DName)

    flag=os.path.exists(DName)
    if flag==False:
        print("Invalid Path")
        exit()
    
    flag=os.path.isdir(DName)
    if flag==False:
        print("Not directory")
        exit()
    
    for Folder,SubFolders,Files in os.walk(DName):
        for FNames in Files:
            FNames=os.path.join(Folder,FNames)
            checksum=CheckSum(FNames)
            print("File name is:",FNames)
            print("CheckSum is:",checksum)
            print()

def main():
    DirName=sys.argv[1]
    DirectoryCheckSum(DirName)


if __name__=="__main__":
    main()
