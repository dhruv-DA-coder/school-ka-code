

# Python code for finding the GCD of two floating numbers.
 
import math
 
# Recursive function to return gcd 
# of a and b
def gcd(a,b) :
    if (a < b) :
        return gcd(b, a)
     
    # base case
    if (abs(b) < 0.001) :
        return a
    else :
        return (gcd(b, a - math.floor(a / b) * b))
     
      
# Driver Function.
a = 1.20
b = 22.5
print('{0:.1f}'.format(gcd(a, b)))
