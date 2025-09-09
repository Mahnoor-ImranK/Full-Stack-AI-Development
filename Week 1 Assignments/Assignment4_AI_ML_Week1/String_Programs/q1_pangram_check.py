#Check if a string is a pangram
import string
s = input("Enter a string: ").lower()
letters = set(ch for ch in s if ch.isalpha())
print(len(letters) == 26)
