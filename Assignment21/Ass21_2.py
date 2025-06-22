import psutil

def ProcInfo(Name):
    border="-"*80
    print(border)
    print("Information of the running process")
    print(border)
    process=[]
    for proc in psutil.process_iter(['name']):
        if proc.info['name']==Name:
            info=proc.as_dict(attrs=['pid','username'])
            info['vms']=proc.memory_info().vms/(1024*1024)
            process.append((info))
            print(info)
            
    if not process:
            print(f"No such process named as {Name} found ")


def main():
    ProcName="ChatGPT.exe"
    ProcInfo(ProcName)


if __name__=="__main__":
    main()