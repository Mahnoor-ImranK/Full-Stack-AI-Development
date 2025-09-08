# Question 3: Calculate Compound Interest
# Formula: compound_interest = P * (1 + R/100)**T - P

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

compound_interest = P * (1 + R/100)**T - P
print("Compound Interest:", compound_interest)
