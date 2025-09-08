# Question 17: Convert Minutes to Hours and Minutes

minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining = minutes % 60

print(minutes, "minutes =", hours, "hours and", remaining, "minutes")
