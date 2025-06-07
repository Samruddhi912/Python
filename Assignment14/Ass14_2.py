class Rectangle:
    def __init__(self,A,B):
        self.lenght=A
        self.breadth=B
    def Area(self):
        Area=self.lenght*self.breadth
        return Area

    def Perimeter(self):
        Perimeter=2*self.lenght*self.breadth
        return Perimeter

def main():
    len=int(input("Enter length"))
    breadth=int(input("Enter breadth"))
    obj1=Rectangle(len,breadth)
    Res=obj1.Area()
    print("Area:",Res)
    Res=obj1.Perimeter()
    print("Area:",Res)

if __name__=="__main__":
    main()
