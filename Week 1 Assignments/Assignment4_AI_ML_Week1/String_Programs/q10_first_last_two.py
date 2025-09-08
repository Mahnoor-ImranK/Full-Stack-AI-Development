    # New string made of first 2 and last 2 chars
s = input('Enter string: ')
if len(s)<2:
    print('Empty or too short')
else:
    print(s[:2]+s[-2:])
