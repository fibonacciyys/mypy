import math

x = math.sin(math.pi/9) #x=sin20度

y1 = 24 * x**4 + 6 - 24 * x**2 + 8 * 3**0.5 * x**3 * (1 - x**2)**0.5
y2 = 3 * (16 * x**4 + 3 - 12 * x**2)**0.5

re = y1 / y2
print(re)