lst=list(map(int, input('Enter list: ').split()))
seen=set(); out=[]
for x in lst:
    if x not in seen:
        seen.add(x); out.append(x)
print(out)
