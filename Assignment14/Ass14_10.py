class Employee:
    def __init__(self,A,B,C):
        self.__salary=A
        self._department=B
        self.Name=C
    def Display(self):
        print("Name of Employee",self.Name)
        print("Department of Employee",self._department)
        print("Salary of Employee",self.__salary)
    
def main():
    obj=Employee(50000,"Comp","John")
    obj.Display()
    #print(obj.__salary)
    print(obj.Name)
    print(obj._department)
    

if __name__=="__main__":
    main()