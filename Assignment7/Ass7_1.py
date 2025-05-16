Square=lambda A:A**2
Cube=lambda A:A**3
def main():
    print("Enter one number")
    num=int(input())
    Res=Square(num)
    print("Square:",Res)
    Res=Cube(num)
    print("Cube:",Res)
if __name__=="__main__":
    main()
