class demo:
    Value=21
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
    def fun(self):
        print("Call from fun function")
        print(self.no1)
        print(self.no2)
    def gun(self):
        print("Call from gun function")
        print(self.no1)
        print(self.no2)
    
def main():
    print("Class variable value:",demo.Value)
    print("Enter two numbers:")
    num1=int(input())
    num2=int(input())
    print("Enter two numbers:")
    num3=int(input())
    num4=int(input())
    obj1=demo(num1,num2)
    obj1.fun()
    obj1.gun()
    obj2=demo(num3,num4)
    obj2.fun()
    obj2.gun()
if __name__=="__main__":
    main()


