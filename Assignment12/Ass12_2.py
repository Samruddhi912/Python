class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circum=0.0
    def Accept(self,Rad):
        self.Radius=Rad
    def CalArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
    def CalCircum(self):
        self.Circum=2*Circle.PI*self.Radius
    def Display(self):
        print("Radius of circle is:",self.Radius)
        print("Area of circle is:",self.Area)
        print("Circumference of circle is:",self.Circum)
def main():
    print("Enter Area:")
    no=int(input())
    obj1=Circle()
    obj1.Accept(no)
    obj1.CalArea()
    obj1.CalCircum()
    obj1.Display()

if __name__=="__main__":
    main()

        
    
