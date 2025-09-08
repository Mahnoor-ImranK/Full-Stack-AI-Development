    # Perfect squares in range whose sum of digits < 10
start=int(input('start: ')); end=int(input('end: '))
res=[]
import math
for i in range(int(math.ceil(start**0.5)), int(math.floor(end**0.5))+1):
    sq=i*i
    if sum(int(d) for d in str(sq))<10:
        res.append(sq)
print(res)
