class Product:
    def __init__(self,A,B):
        self.name=A
        self.price=B
    def __eq__(self, otherprice):
        if isinstance(otherprice,Product):
            return self.price==otherprice.price
        return False
    
def main():
    obj=Product("Milk",56)
    obj2=Product("Bread",40)
    obj3=Product("Egg",56)
    print(obj==obj2)
    print(obj==obj3)
    

if __name__=="__main__":
    main()