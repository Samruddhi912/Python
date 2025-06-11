import sys

def main():
    FName=sys.argv[1]
    fobj=open(FName,"w")
    Ip=[]
    print("enter number of elements you want to enter")
    num=int(input())
    print("Enter numbers you want  to write in file")
    for i in range (num):
        no=int(input())
        fobj.write(str(no)+"\n")
        Ip.append(no)
    fobj.close()
    fobj=open(FName,"r")
    data=fobj.read()
    print(data)

if __name__=="__main__":
    main()