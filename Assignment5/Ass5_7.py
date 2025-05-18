def Area(Num1,Num2):
    Ans=Num1*Num2
    return Ans

def Perimeter(Num1,Num2):
    Ans=2*(Num1+Num2)
    return Ans 
    
def main():
    print("Enter a Length")
    no1=int(input())
    print("Enter a Width")
    no2=int(input())
    Res=Area(no1,no2)
    print("Area:",Res)
    Res=Perimeter(no1,no2)
    print("Perimeter:",Res)
    
    

if __name__=="__main__":
    main()