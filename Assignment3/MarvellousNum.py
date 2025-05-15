def ChkPrime(isNumPrime):    
    for i in range(2,isNumPrime):
        if(isNumPrime%i==0):
            return False
    return True
            