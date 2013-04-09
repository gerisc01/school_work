import math

def madhava(n):
    theSum = 0
    for i in range(n):
        theSum = theSum + ((math.sqrt(12))*(1/((2*i+1)*((-3)**i))))
    return theSum

print(madhava(6))
print(madhava(9))
print(madhava(150))
