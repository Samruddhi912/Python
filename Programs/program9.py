def NumMax(num1,num2,num3):
    if((num1>num2) and (num1>num3)):
        return num1; 

    elif((num2>num1) and (num2>num3)):
        return num2; 

    elif((num3>num1) and (num3>num2)):
        return num3; 

def main():
    print("Enter three numbers")
    no1=int(input())
    no2=int(input())
    no3=int(input())

    ans=NumMax(no1,no2,no3)
    print(f"Largest number from {no1} , {no2} , {no3} is : {ans}")

if __name__=="__main__":
    main()