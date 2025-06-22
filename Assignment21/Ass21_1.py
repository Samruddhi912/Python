
import psutil

def procInfo():
    Border="-"*80
    print(Border)
    print("Information of running processes")
    print(Border)
    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=['name','pid','username'])
        info['vms']=proc.memory_info().vms/(1024*1024)
        print(info)

def main():
    procInfo()
    

if __name__=="__main__":
    main()
