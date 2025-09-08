    # Armstrong check
n=int(input('Enter number: '))
s=str(n); k=len(s)
if sum(int(ch)**k for ch in s)==n:
    print('It is an Armstrong number')
else:
    print('Not an Armstrong number')
