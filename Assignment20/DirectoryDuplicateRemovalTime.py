import sys
import os
import time
import hashlib

def CalculateCheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")
    hobj=hashlib.md5()
    buffer=fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)

    fobj.close()
    return hobj.hexdigest()

def DirectoryDuplicate(DName):
    flag=os.path.isabs(DName)
    if flag==False:
        DName=os.path.abspath(DName)

    flag=os.path.exists(DName)
    if flag==False:
        exit()

    flag=os.path.isdir(DName)
    if flag==False:
        exit()
    Duplicate={}
    for Folder,SubFolders,Files in os.walk(DName):
        for FNames in Files:
            FNames=os.path.join(Folder,FNames)
            checksum=CalculateCheckSum(FNames)
            if checksum in Duplicate:
                Duplicate[checksum].append(FNames)
            else:
                Duplicate[checksum]=[FNames]
    return Duplicate

def DirectoryRemoval(MyDict):
    Count=0
    Res=list(filter(lambda x:len(x)>1,MyDict.values()))
    for value in Res:
        for subvalues in value:
            Count+=1
            if Count>1:
                os.remove(subvalues)
    
    timestamp=time.ctime()
    fileName="Marvellous%sLog.log" %(timestamp)
    fileName=fileName.replace(":","_")
    fileName=fileName.replace(" ","_")
    fobj=open(fileName,"w")
    fobj.write("File create at:"+time.ctime())
    fobj.write("\n\n")
    fobj.write("Total files deleted are:"+str(Count))

    fobj.close()


def main():
    StartTime=time.time()
    DirName=sys.argv[1]
    Result=DirectoryDuplicate(DirName)
    DirectoryRemoval(Result)
    EndTime=time.time()
    print("Total time needed for Execution of Script is:",EndTime-StartTime)

if __name__=="__main__":
    main()