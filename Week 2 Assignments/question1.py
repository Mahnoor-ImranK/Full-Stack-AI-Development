# Question 1
import pandas as pd

#sample data
data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

#create DataFrame
df1 = pd.DataFrame(data)

#display DataFrame
print("DataFrame from Dictionary:")
print(df1)
