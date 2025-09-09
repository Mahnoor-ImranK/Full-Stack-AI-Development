#Find larger string without built-ins (compare lengths manually)
s1 = input('String 1: ')
s2 = input('String 2: ')
#manual length
l1=l2=0
for _ in s1: l1+=1
for _ in s2: l2+=1
if l1>l2: print('Larger:', s1)
elif l2>l1: print('Larger:', s2)
else: print('Equal length')
