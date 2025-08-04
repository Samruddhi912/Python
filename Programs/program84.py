class Demo:
    def __init__(self,A,B):
        print("Inside Constructor")
        self.No1=A
        self.No2=B
    
    def __del__(self):
        print("Inside destructor")
    
    def Display(self):
        print("Value of No1 is:",self.No1)
        print("Value of No2 is:",self.No2)

def main():
    print("Inside main")
    obj1=Demo(10,20)
    obj2=Demo(11,21)
    obj1.Display()

    print("End")

if __name__=="__main__":
    main()