    # LCM of two numbers
import math
x=int(input('a: ')); y=int(input('b: '))
print('LCM:', abs(x*y)//math.gcd(x,y))
