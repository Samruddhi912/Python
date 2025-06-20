import os
import sys
import hashlib
import time

def CalculateCheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")
    hobj=hashlib.md5()
    buffer=fobj.read(BlockSize)
    while (len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)
    
    fobj.close()
    return hobj.hexdigest()

def DirectoryDuplicateDelete(DName):
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
        for Fnames in Files:
            Fnames=os.path.join(Folder,Fnames)
            checksum=CalculateCheckSum(Fnames)
            if checksum in Duplicate:
                Duplicate[checksum].append(Fnames)
            else:
                Duplicate[checksum]=[Fnames]
    return Duplicate

def DeleteDuplicate(MyDict):        
    Res=list(filter(lambda x:len(x)>1,MyDict.values()))
    count=0
    cnt=0
    for value in Res:
        for subvalue in value:
            count+=1
            if count>1:
                print("Deleted File is:",subvalue)
                os.remove(subvalue)
                cnt+=1
        count=0
    

    timestamp=time.ctime()
    fileName="Marvellous%sLog.log"%(timestamp)
    fileName=fileName.replace(":","_")
    fileName=fileName.replace(" ","_")
    
    fobj=open(fileName,"w")
    fobj.write("File is created at:"+time.ctime())
    fobj.write("\n\n")
    fobj.write("Total Count of Files is:"+str(count))
    fobj.write("\n\n")
    fobj.write("Total deleted files are:"+str(cnt))


def main():
    DirName=sys.argv[1]
    Result=DirectoryDuplicateDelete(DirName)
    DeleteDuplicate(Result)

if __name__=="__main__":
    main()