

def main():
    print("Enter File name:")
    fName=input()
    fobj=open(fName,"w")
    fobj.write("Hello")
    fobj=open(fName,"r")
    data=fobj.read()
    print(data)
    fobj.close()


if __name__=="__main__":
    main()