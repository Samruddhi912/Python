import os
def ChkDir(FileName):
    flag=os.path.exists(FileName)
    if flag==True:
        return True
    else:
        return False


def main():
    print("Enter File name:")
    fName=input()
    fobj=open("Demo.txt","w")
    fobj.write("Hello")
    fobj.close()
    Res=ChkDir(fName)
    if Res==True:
        print(fName,"Exists")
    else:
        print(fName,"does not Exists")

if __name__=="__main__":
    main()
