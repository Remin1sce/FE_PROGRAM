from math import gcd
class Fraction:
    def __init__(self,a,b):
        # Your code here
        gcd_v = gcd(a,b)
        self.a = a/gcd_v
        self.b = b/gcd_v
        
    def __str__(self):
        # Your code here

    def __eq__(self,p):
        return self.a == p.a and self.b == p.b

    def __add__(self,p):
        up = (self.a*p.b)
        pass
        return Fraction()

    def __sub__(self,p):
        # Your code here
        
    def __mul__(self,p):
        # Your code here

    def __truediv__(self,p):
        # Your code here

# Do not change the code below this line.
p = Fraction(int(input()),int(input()))
q = Fraction(int(input()),int(input()))
r = Fraction(int(input()),int(input()))
s = (p/q)*(p+q) - q
print(s)
print(s==r)