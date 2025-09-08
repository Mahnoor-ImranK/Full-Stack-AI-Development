    lst=list(map(int, input('Enter list: ').split()))
evens=[x for x in lst if x%2==0]
odds=[x for x in lst if x%2!=0]
print('Largest even:', max(evens) if evens else None)
print('Largest odd:', max(odds) if odds else None)
