# Question 7: Distribute Items Equally

candies = int(input("Enter number of candies: "))
students = int(input("Enter number of students: "))

each = candies // students
left = candies % students

print("Each student gets:", each)
print("Candies left:", left)
