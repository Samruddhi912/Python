class BookStore:
    NoOfBooks=0
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
    def Display(self):
        print("Name of Book:",self.Name)
        print("Name of Author:",self.Author)
        print("Number of Book:",BookStore.NoOfBooks)

def main():
    Obj1=BookStore('Linux Programming','Robert Love')
    Obj1.Display()
    Obj2=BookStore('C Programming','Dennis Ritchie')
    Obj2.Display()

if __name__=="__main__":
    main()
