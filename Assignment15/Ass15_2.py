def main():
    print("Enter file name:")
    fName=input()
    fobj=open(fName,"w")
    fobj.write("Hellooo!!!! My name is Samruddhi Kadam")
    fobj=open(fName,"r")
    data=fobj.read()
    print("Contents of the File are:",data)
    fobj.close()

if __name__=="__main__":
    main()