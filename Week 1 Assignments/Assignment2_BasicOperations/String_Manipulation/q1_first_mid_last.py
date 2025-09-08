# Q1: Create new string from first, middle, last character
s = input("Enter a string: ")
if len(s) >= 3:
    mid = len(s)//2
    print(s[0] + s[mid] + s[-1])
else:
    print("String too short")
