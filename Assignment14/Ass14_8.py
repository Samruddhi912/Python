class Vehicle:
    def __init__(self,A):
        print("Inside Vehicle Constructor")
        self.Name=A
    def start(self,Mode):
        self.Model=Mode
class Car(Vehicle):
    def __init__(self,A):
        super().__init__(A)
    def start(self,Mode,TY):
        self.Model=Mode
        self.Type=TY

def main():
    obj=Car("Scorpio")
    obj.start("Sedan","EV")
    print("Vehicle Name:",obj.Name)
    print("Model of Vehicle:",obj.Model)
    print("Type of vehicle:",obj.Type)

if __name__=="__main__":
    main()