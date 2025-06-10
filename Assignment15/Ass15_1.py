import os
def ChkDirectory(fDir):
    flag=os.path.exists(fDir)
    if flag==True:
        return True
    else:
        return False

def main():
    print("Enter name of file:")
    fName=input()
    Res=ChkDirectory(fName)
    if Res==True:
        print("File exists")
    else:
        print("File doesn't exists")

if __name__=="__main__":
    main()
