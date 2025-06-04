class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
    def Accept(self,Num1,Num2):
        self.Value1=Num1
        self.Value2=Num2
    def Addition(self):
        Ans=0
        Ans=self.Value1+self.Value2
        return Ans
    def Substraction(self):
        Ans=0
        Ans=self.Value1-self.Value2
        return Ans
    def Multiplication(self):
        Ans=0
        Ans=self.Value1*self.Value2
        return Ans
    def Division(self):
        Ans=0
        Ans=self.Value1/self.Value2
        return Ans
def main():
    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))
    obj1=Arithmetic()
    obj1.Accept(no1,no2)
    Res=obj1.Addition()
    print("Addition is:",Res)
    Res=obj1.Substraction()
    print("Substraction is:",Res)
    Res=obj1.Multiplication()
    print("Multiplication is:",Res)
    Res=obj1.Division()
    print("Division is:",Res)
if __name__=="__main__":
    main()
