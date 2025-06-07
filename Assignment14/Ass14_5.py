class BankAcc:
    def __init__(self,A,B,C):
        self.AccNo=A
        self.Name=B
        self.Balance=C
    def Deposit(self,AmtDep):
        self.Balance=self.Balance+AmtDep
    def WithDraw(self,AmtWith):
        self.Balance=self.Balance-AmtWith
    def Display(self):
        print("AccountNumber:",self.AccNo)
        print("Total Balance:",self.Balance)
        
def main():
    obj=BankAcc(101,"Shashank",10000)
    obj.Deposit(500)
    obj.WithDraw(200)
    obj.Display()

if __name__=="__main__":
    main()