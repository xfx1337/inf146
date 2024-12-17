import math

# поиск корней уравнения типа F(x)=0
# метод секущих

def f(x):
   return x**2+3*x-2

def get_ends(f, a, b, h):
   ls = []
   while a < b:
      if f(a) * f(a+h) < 0:
         ls.append((a,a + h))
      a += h
   return ls

def sec(f, a, b, h):
   x = a
   while abs(f(b) - f(x)) > h:
      b = x - (f(x) * (b - x) / (f(b) - f(a)))
      x = b
   return b


ls = get_ends(f, -1, 10, 0.01)
for t in ls:
   print(sec(f, t[0], t[1], 0.0000001))