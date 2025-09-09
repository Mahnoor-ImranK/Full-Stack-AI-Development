#Count uppercase and lowercase letters
s = input('Enter string: ')
up=sum(1 for c in s if c.isupper())
low=sum(1 for c in s if c.islower())
print('Upper:', up, 'Lower:', low)
