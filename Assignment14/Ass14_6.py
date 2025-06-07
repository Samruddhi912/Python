class Calculator:
    def __init__(self,A,B):
        self.Num1=A
        self.Num2=B

    def Add(self):
        Ans=0
        Ans=self.Num1+self.Num2
        return Ans
    def Subtract(self):
        Ans=0
        Ans=self.Num1-self.Num2
        return Ans 
    def Multily(self):
        Ans=0
        Ans=self.Num1*self.Num2
        return Ans
    def Divide(self):
        Ans=0
        Ans=self.Num1/self.Num2
        return Ans
    
        
def main():
    no1=int(input("Enter first Number:"))
    no2=int(input("Enter Second Number:"))
    obj=Calculator(no1,no2)
    Res=obj.Add()
    print("Addition is:",Res)
    Res=obj.Subtract()
    print("Subtraction is:",Res)
    Res=obj.Multily()
    print("Multiplication is:",Res)
    Res=obj.Divide()
    print("Division is:",Res)
    

if __name__=="__main__":
    main()