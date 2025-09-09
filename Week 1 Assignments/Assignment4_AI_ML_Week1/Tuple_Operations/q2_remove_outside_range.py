tuples = [(10,'a'), (20,'b'), (30,'c'), (40,'d')]
low=int(input('low: ')); high=int(input('high: '))
print([t for t in tuples if low<=t[0]<=high])
