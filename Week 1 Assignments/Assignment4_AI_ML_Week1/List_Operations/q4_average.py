lst=list(map(float, input('Enter numbers: ').split()))
print(sum(lst)/len(lst) if lst else 0)
