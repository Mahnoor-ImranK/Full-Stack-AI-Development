#Check amicable numbers
import math

def sum_proper(n):
    s=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s+=i
            if i!=n//i: s+=n//i
    return s

x=int(input('x: ')); y=int(input('y: '))
print(sum_proper(x)==y and sum_proper(y)==x)
