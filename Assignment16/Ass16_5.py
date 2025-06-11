def Display(fileName):
    obj=open(fileName,"r")
    for line in obj:
        word=line.split()
        if len(word)>5:
            print(line)

    obj.close()

def main():
    print("Enter file Name:")
    FName=input()
    fobj=open(FName,"w")
    fobj.write("India is my Country\nAll Indians are my bothers and Sisters\nI love my country and i am proud of its rich and varied heritage")
    fobj.close()
    Display(FName)

if __name__=="__main__":
    main()