class Book:
    def __init__(self,A):
        self.__price=A
    def Display(self):
        #self.__price=101
        print("Price of Book is:",self.__price)

def main():
    obj=Book(10)
    obj.Display()
    #print(obj.__price)
if __name__=="__main__":
    main()