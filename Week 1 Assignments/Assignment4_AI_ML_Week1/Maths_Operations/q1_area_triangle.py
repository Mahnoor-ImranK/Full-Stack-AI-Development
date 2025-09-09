#Area of triangle given sides using Heron's formula
import math
a=float(input('a: ')); b=float(input('b: ')); c=float(input('c: '))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area:', area)
