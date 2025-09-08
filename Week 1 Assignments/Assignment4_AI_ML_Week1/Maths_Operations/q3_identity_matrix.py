    # Identity matrix
n=int(input('n: '))
for i in range(n):
    row = ['1' if i==j else '0' for j in range(n)]
    print(' '.join(row))
