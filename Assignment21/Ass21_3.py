import psutil
import time
import sys
import os

def ProcInfoLof():
    
    process=[]
    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=["name","pid","username"])
        info["vms"]=proc.memory_info().vms/(1024*1024)
        process.append(info)
        return info
    
def Directory(DName,ProcInfo):
    border="-"*80
    time_stamp=time.ctime()
    if not os.path.exists(DName):
        os.makedirs(DName)

    FileName="ProcessInformation%s.Log" %(time_stamp)
    FileName=FileName.replace(":","_")
    FileName=FileName.replace("/","_")
    FileName=FileName.replace(" ","_")
    filePath=os.path.join(DName,FileName)
    fobj=open(filePath,"w")
    fobj.write(border+"\n")
    fobj.write(f"File created at: {time_stamp}\n")
    fobj.write(str(ProcInfo))
    fobj.write("\n")
    fobj.write(border)



def main():
    DirName=sys.argv[1]
    Result=ProcInfoLof()
    Directory(DirName,Result)


if __name__=="__main__":
    main()