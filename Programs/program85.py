class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
    
    def Add(self):
        Ans=0
        Ans=self.No1+self.No2
        return Ans
    
    def Substract(self):
        Ans=0
        Ans=self.No1-self.No2
        return Ans

def main():
    obj1=Arithematic(21,11)
    Ret=obj1.Add()
    print("Addition is:",Ret)
    Ret=obj1.Substract()
    print("Substraction is:",Ret)
    obj2=Arithematic(100,50)
    Ret=obj2.Add()
    print("Addition is:",Ret)
    Ret=obj2.Substract()
    print("Substraction is:",Ret)

if __name__=="__main__":
    main()