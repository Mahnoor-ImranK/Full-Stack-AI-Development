#Add new item after specified item
lst = ['apple','banana','cherry']
target = 'banana'
new = 'mango'
if target in lst:
    lst.insert(lst.index(target)+1, new)
print(lst)
