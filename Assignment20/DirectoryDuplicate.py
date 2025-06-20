import sys
import os
import time
import hashlib
def CalculateCheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()
    buffer=fobj.read(BlockSize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)
    fobj.close()
    
    return hobj.hexdigest()

def DirectoryDuplicate(DirName):
    timestamp=time.ctime()
    flag=os.path.isabs(DirName)
    if flag==False:
        DirName=os.path.abspath(DirName)

    flag=os.path.exists(DirName)
    if flag==False:
        exit()

    flag=os.path.isdir(DirName)
    if flag==False:
        exit()

    Duplicate={}

    for Folder,SubFolders,Files in os.walk(DirName):
        for Fnames in Files:
            Fnames=os.path.join(Folder,Fnames)
            checksum=CalculateCheckSum(Fnames)
            if checksum in Duplicate:
                Duplicate[checksum].append(Fnames)
            else:
                Duplicate[checksum]=[Fnames]
    
    fileName="MarvellousLog%s.log" %(timestamp)
    fileName=fileName.replace(":","_")
    fileName=fileName.replace(" ","_")
    fileName=fileName.replace("/","_")

    fobj=open(fileName,"w")
    fobj.write("This file is created at:"+time.ctime())
    fobj.write("\n\n")
    fobj.write(str(Duplicate))

def main():
    DName=sys.argv[1]
    DirectoryDuplicate(DName)

if __name__=="__main__":
    main()