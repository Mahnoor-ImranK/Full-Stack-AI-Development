#Replace item if found
lst = ['apple','banana','cherry']
old = 'banana'
new = 'grapes'
lst = [new if x==old else x for x in lst]
print(lst)
