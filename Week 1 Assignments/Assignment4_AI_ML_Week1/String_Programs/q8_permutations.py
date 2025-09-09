#Print permutations in lexicographic order without recursion
from itertools import permutations
s = input('Enter string (unique chars preferred): ')
perms = sorted(''.join(p) for p in permutations(s))
for p in perms:
    print(p)
