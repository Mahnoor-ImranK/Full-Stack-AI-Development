#Delete list of keys
d = {'a':1,'b':2,'c':3,'d':4}
keys = ['b','d']
for k in keys:
    d.pop(k, None)
print(d)
