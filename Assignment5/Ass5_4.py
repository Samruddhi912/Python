def ChkMax(Num1,Num2,Num3):
    if (Num1>Num2 and Num1>Num3):
        return Num1
    elif (Num2>Num1 and Num2>Num3):
        return Num2
    elif (Num3>Num1 and Num3>Num2):
        return Num3
    
def main():
    print("Enter three numbers")
    no1=int(input())
    no2=int(input())
    no3=int(input())
    Res=ChkMax(no1,no2,no3)
    print("Largest number is:",Res)

if __name__=="__main__":
    main()