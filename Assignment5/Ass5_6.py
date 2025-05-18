def Converter(Temp):
    Fahren=(Temp*9/5)+32
    return Fahren
    
def main():
    print("Enter a temperature in Celcius")
    Cel=int(input())
    Res=Converter(Cel)
    print("Temperature in Fahrenheit is",Res,"F")

if __name__=="__main__":
    main()