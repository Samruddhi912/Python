class BankAccount:
    ROI=10.5
    def __init__(self,A,B):
        self.Name=A
        self.Amount=B
    def Deposit(self,Amt):
        Amt=self.Amount+Amt
        print('Amount Deposited is:',Amt)
    def Withdraw(self,WithAmt):
        WithAmt=self.Amount-WithAmt
        print('Amount Withdrawed is:',WithAmt)
    def CalInterest(self):
        InterstAmt=self.Amount*BankAccount.ROI
        print('Interested Amount is:',InterstAmt)
    def Display(self):
        print("Name of Customer:",self.Name)
        print("Amount of Customer:",self.Amount)

def main():

    obj1=BankAccount("Sam",1000)
    obj1.Deposit(100)
    obj1.Withdraw(250)
    obj1.CalInterest()
    obj1.Display()

    obj1=BankAccount("Pankaj",2000)
    obj1.Deposit(10)
    obj1.Withdraw(50)
    obj1.CalInterest()
    obj1.Display()



if __name__=="__main__":
    main()