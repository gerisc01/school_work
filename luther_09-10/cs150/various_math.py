#Scott Gerike
#CS 150
#9/21/09
#trying out math module

import math

def circumference(n):
    return 2*math.pi*n

circ = circumference

def area(n):
    return math.pi*n**2

def volume(n):
    return (4/3)*math.pi*n**3

print(circ(5))
print(circ(8))
print(area(9))
print(area(2))
print(area(17))
print(volume(4))
print(volume(7))
print(volume(9))



