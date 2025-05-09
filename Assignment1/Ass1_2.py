def ChkNum(Num):
    if((Num%2)==0):
        return True
    else:
        return False

def main():
    print("Enter one number")
    no1=int(input())
    Result=ChkNum(no1)
    if(Result==True):
        print("The number",no1,"is Even Number")
    else:
        print("The number",no1,"is Odd Number")
 
if __name__=="__main__":
    main()