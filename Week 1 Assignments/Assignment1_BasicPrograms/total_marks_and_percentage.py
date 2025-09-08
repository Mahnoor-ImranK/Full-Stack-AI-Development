# Question 9: Total Marks and Percentage

marks = []
for i in range(5):
    m = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100
average = total / 5

print("Total Marks:", total)
print("Percentage:", percentage)
print("Average:", average)
