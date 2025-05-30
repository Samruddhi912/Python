import threading
def EvenFact(no):
    Fact=1
    for i in range (1,no+1):
        if (no%i==0):
            if(i%2==0):
                Fact=Fact+i
    print("Addition",Fact)
    
def OddFact(no):
    Fact=1
    for i in range (1,no+1):
        if (no%i==0):
            if(i%2!=0):
                Fact=Fact+i
    print("Addition",Fact)

def main():
    print("Enter even number")
    num1=int(input())
    print("Enter odd number")
    num2=int(input())
    T1=threading.Thread(target=EvenFact,args=(num1,))
    T2=threading.Thread(target=OddFact,args=(num2,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print("Exist from main")

if __name__=="__main__":
    main()