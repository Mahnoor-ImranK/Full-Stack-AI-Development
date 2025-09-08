# Q2: Count occurrences of all characters
s = input("Enter a string: ")
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
for k,v in counts.items():
    print(f"{k!r}: {v}")
