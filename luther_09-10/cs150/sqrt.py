#Scott Gerike
#CS150
#9/21/09
#Calculating Square Roots using Newton's method

def squareroot(n,numterms):
    answer = 1
    for counter in range(numterms):
        answer = (1/2)*(answer + (n/answer))

    return answer

print(squareroot(100,20))
print(squareroot(155,10))
print(squareroot(29,50))

