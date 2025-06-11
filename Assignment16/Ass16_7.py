def Marks(fileName):
    obj=open(fileName,"r")
    for line in obj:
        if "Marks:" in line:
            marks=int(line.split("Marks:")[1])
            if marks>75:
                print(line.strip())
        

def main():
    print("Enter file Name:")
    FName=input()
    fobj=open(FName,"w")
    fobj.write("Name:Samruddhi-Marks:80\nName:Raj-Marks:60\nName:Om-Marks:76\nName:Piyush-Marks:89")
    fobj.close()
    Marks(FName)
    

if __name__=="__main__":
    main()