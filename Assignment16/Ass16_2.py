import sys
def main():
    FName=sys.argv[1]
    fobj=open(FName,"r")
    data=fobj.read()
    print(data)
    
if __name__=="__main__":
    main()