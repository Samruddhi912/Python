class Numbers:
    def __init__(self,A):
        self.Value=A
    def ChkPrime(self):
        for i in range(2,self.Value):
            if(self.Value%i==0):
                return False
            return True
    def ChkPerfect(self):
        pass
    def Factors(self):
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                print(i)
    def SumFact(self):
        Sum=0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                Sum=Sum+i
        return Sum
def main():
    obj1=Numbers(11)
    Res=obj1.ChkPrime()
    if Res==True:
        print("It is a prime number")
    else:
        print("It is not a prime number")
    obj1.Factors()
    Res=obj1.SumFact()
    print("Sum of Factors is:",Res)

    obj2=Numbers(101)
    Res=obj2.ChkPrime()
    if Res==True:
        print("It is a prime number")
    else:
        print("It is not a prime number")
    obj2.Factors()
    Res=obj2.SumFact()
    print("Sum of Factors is:",Res)

    obj3=Numbers(24)
    Res=obj3.ChkPrime()
    if Res==True:
        print("It is a prime number")
    else:
        print("It is not a prime number")
    obj3.Factors()
    Res=obj3.SumFact()
    print("Sum of Factors is:",Res)

if __name__=="__main__":
    main()