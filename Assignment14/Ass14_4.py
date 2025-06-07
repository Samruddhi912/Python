class Student:
    school_name="ABC"
    def __init__(self,A,B):
        self.name=A
        self.roll=B
    def Display(self):
        print("Name of Student:",self.name)
        print("School Name is:",self.school_name)
def main():
    Student.school_name="RamBhau School"
    obj=Student("Sam",101)
    obj.Display()

if __name__=="__main__":
    main()