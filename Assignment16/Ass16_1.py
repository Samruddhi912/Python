def main():
    print("Enter file name you want to create:")
    FName=input()
    fobj=open(FName,"w")
    fobj.write("1.Samruddhi Kadam\n2.Pankaj Andhare\n3.Om Kadam\n4.Mayank Salunkhe\n5.Riya Jadhav")
    fobj.close()
    fobj=open(FName,"r")
    data=fobj.read()
    print(data)
    fobj.close()

if __name__=="__main__":
    main()
