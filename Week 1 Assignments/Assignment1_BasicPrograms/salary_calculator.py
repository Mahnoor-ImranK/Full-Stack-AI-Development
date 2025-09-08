# Question 10: Salary Calculator

basic = float(input("Enter Basic Salary: "))
HRA = 0.20 * basic
DA = 0.15 * basic
total = basic + HRA + DA

print("HRA:", HRA)
print("DA:", DA)
print("Total Salary:", total)
