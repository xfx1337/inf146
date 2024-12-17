from cmath import *

class Complex:
    def __init__(self, r, m):
        self.r = r
        self.m = m
    
    def __add__(self,o):
        return Complex(self.r + o.r, self.m + o.m)
    def __sub__(self, o):
        return Complex(self.r - o.r, self.m - o.m)
    def __mul__(self, o):
        if isinstance(o, Complex):
            return Complex(self.r*o.r - (self.m*o.m), self.r*o.m+self.m*o.r)
        elif isinstance(o, complex):
            return Complex(self.r*o.real - (self.m*o.imag), self.r*o.imag+self.m*o.real)
        else:
            return Complex(self.r*o, self.m)
    def __truediv__(self, o):
        return Complex((self.r*self.m+o.r*o.m)/(self.m**2+o.m**2), (self.m*o.r-self.r*o.m)/(self.m**2+o.m**2))
    def __str__(self):
        if self.m == 0 and self.r != 0:
            return f"{self.r}"
        if self.m != 0 and self.r == 0:
            return f"{self.m}i"

        if self.m != 0 and self.r != 0:
            if self.m > 0:
                return f"{self.r} + {self.m}i"
            else:
                return f"{self.r} - {abs(self.m)}i"
        else:
            return "0"
    def __eq__(self, other):
        if isinstance(other, complex):
            return (self.r == other.real and self.m == other.imag)
        elif isinstance(other, Complex):
            return (self.r == other.r and self.m == other.m)
        else:
            raise TypeError("Wrong type. Only complex and Complex are allowed")
         

a = Complex(2, 3)
b = Complex(3, 6)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a==b)
print(a==a)
print(a==complex(2,3))
print(a*2)
print(a*complex(3,6))