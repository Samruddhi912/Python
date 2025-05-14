import Arithematic

def main():
    print("Enter two numbers: ")
    no1=int(input())
    no2=int(input())
    result=Arithematic.Add(no1,no2)
    print("Addition is : ",result)
    result=Arithematic.Sub(no1,no2)
    print("Substraction is : ",result)
    result=Arithematic.Mult(no1,no2)
    print("Multiplication is : ",result)
    result=Arithematic.Div(no1,no2)
    print("Division is : ",result)

if __name__=="__main__":
    main()
