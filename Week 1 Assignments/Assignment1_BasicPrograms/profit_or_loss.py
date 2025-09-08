# Question 8: Calculate Profit or Loss

cost = float(input("Enter Cost Price: "))
sell = float(input("Enter Selling Price: "))

if sell > cost:
    print("Profit:", sell - cost)
elif cost > sell:
    print("Loss:", cost - sell)
else:
    print("No Profit No Loss")
