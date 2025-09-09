#Remove special symbols/punctuation
import string
s = input("Enter a string: ")
allowed = set(string.ascii_letters + string.digits + ' ')
cleaned = ''.join(ch for ch in s if ch in allowed)
print(cleaned)
