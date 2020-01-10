import math
def isPrime(n):
    for i in range(2,math.ceil(math.sqrt(n))):
        if(n % i == 0):
            return False
    return True
        
isPrime(19)