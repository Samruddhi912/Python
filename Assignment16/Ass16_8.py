import shutil
def main():
    
    fobj=open("Basic.txt","w")
    fobj.write("Hello!\n\n\nMy Name is Samruddhi Kadam\n\nThis is File Handling code\n\nWelcome!\n\nUser!!!")
    fobj.close()
    
    fobj=open("Basic.txt","r")
    cleanLines=[]
    for line in fobj:
        if line.strip():
            cleanLines.append(line)
    print(cleanLines)


if __name__=="__main__":
    main()