    lst=list(input('Enter items separated by space: ').split())
if len(lst)>1:
    lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
