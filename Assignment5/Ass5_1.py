import Arithematic
def main():
    print("Enter two numbers from user:")
    no1=int(input())
    no2=int(input())
    Res=Arithematic.Sum(no1,no2)
    print("Sum:",Res)
    Res=Arithematic.Difference(no1,no2)
    print("Difference:",Res)
    Res=Arithematic.Product(no1,no2)
    print("Product:",Res)
    Res=Arithematic.Division(no1,no2)
    print("Division:",Res)

if __name__=="__main__":
    main()
