a=list(map(int, input('List A: ').split()))
b=list(map(int, input('List B: ').split()))
print(sorted(set(a)|set(b)))
