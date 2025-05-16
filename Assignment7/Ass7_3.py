Even=lambda A:A%2==0
def main():
    Data=[]
    print("Number of elements you want to enter")
    num=int(input())
    print("Enter elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("Original List:",Data)
    
    fData=list(filter(Even,Data))
    print(fData)
if __name__=="__main__":
    main()
