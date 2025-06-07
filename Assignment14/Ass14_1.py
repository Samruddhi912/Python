class Employee:
    def __init__(self,A,B,C):
        self.Name=A
        self.Emp_Id=B
        self.salary=C
    def Display(self):
        print("Name of Employee:",self.Name)
        print("ID of Employee:",self.Emp_Id)
        print("Salary of Employee:",self.salary)
def main():
    obj1=Employee("Rohit",101,50000)
    obj1.Display()

    obj2=Employee("Pankaj",201,100000)
    obj2.Display()

if __name__=="__main__":
    main()
