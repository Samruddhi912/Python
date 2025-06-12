import sys
def wordcount(FileName,targetword):
    
    fobj=open(FileName,"w")
    fobj.write("India is my country\nI am proud to be citizen of India\nI love India ")
    fobj.close()
    fobj=open(FileName,"r")
    data=fobj.read().split()
    count_word=0
    for word in data:
        if word==targetword:
            count_word+=1
    
    return count_word

def main():
    Fname=sys.argv[1]
    Res=wordcount(Fname,"India")
    print("Frequency is:",Res)
    


if __name__=="__main__":
    main()