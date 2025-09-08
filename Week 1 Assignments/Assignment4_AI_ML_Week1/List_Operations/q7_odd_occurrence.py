    lst=list(map(int, input('Enter list: ').split()))
from collections import Counter
for k,v in Counter(lst).items():
    if v%2==1:
        print(k); break
