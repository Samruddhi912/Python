class Person:
    def __init__(self,A,B):
        self.Name=A
        self.Age=B
class Teacher(Person):
    def __init__(self, A, B,P,Q):
        super().__init__(A, B)
        self.Subject=P 
        self.Salary=Q
        print("Name of Person:",self.Name)
        print("Age of Person:",self.Age)
        print("Name of Subject:",self.Subject)
        print("Salary of Teacher:",self.Salary)

def main():
    obj=Teacher("Bob",35,"Maths",40000)

if __name__=="__main__":
    main()