    lst = list(map(int, input('Enter numbers: ').split()))
uniq = sorted(set(lst), reverse=True)
print(uniq[1] if len(uniq)>1 else 'No second largest')
