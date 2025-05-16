from functools import reduce
Product=lambda A,B:A*B
def main():
    Data=[]
    print("Number of elements you want to enter")
    num=int(input())
    print("Enter elements")
    for i in range(num):
        no=int(input())
        Data.append(no)
    print("Original List:",Data)
    
    rData=(reduce(Product,Data))
    print(rData)
if __name__=="__main__":
    main()
