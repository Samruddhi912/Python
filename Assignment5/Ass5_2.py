def ChkChar(Letter):
    if(Letter=='a' or Letter=='e' or Letter=='i' or Letter=='o' or Letter=='u' or Letter=='A' or Letter=='E' or Letter=='I' or Letter=='O' or Letter=='U' ):
        return True
    else:
        return False
def main():
    print("Enter a character")
    Char=input()
    Res=ChkChar(Char)
    if Res==True:
        print(Char,"is a vowel")
    else:
        print(Char,"is a constant")

if __name__=="__main__":
    main()