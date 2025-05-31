def Display(Value):
    if(Value>=1):
        print(Value)
        Value=Value-1
        Display(Value)

def main():
    no=int(input("Enter number:"))
    Display(no)


if __name__=="__main__":
    main()
