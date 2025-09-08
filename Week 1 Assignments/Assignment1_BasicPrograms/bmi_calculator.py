# Question 16: Calculate Body Mass Index (BMI)

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)
print("BMI:", bmi)
