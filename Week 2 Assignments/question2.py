# Question 2
import pandas as pd
import numpy as np

#sample data
data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9,
              20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2,
                 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']

#create DataFrame
df2 = pd.DataFrame(data, index=labels)

# Question 2
print("Data Frame:\n", df2, "\n")

# Question 2.1 - Summary info
print("Summary Info:")
print(df2.info(), "\n")

# Question 2.2 - First 3 rows
print("First 3 Rows:")
print(df2.head(3), "\n")

# Question 2.3 - Select 'name' and 'score' columns
print("'name' and 'score' Columns:")
print(df2[['name', 'score']], "\n")

# Question 2.4 - 'name' and 'score' columns in rows 1,3,5,6
print("Specific Rows and Columns:")
print(df2.loc[['b','d','f','g'], ['name','score']], "\n")

# Question 2.5 - Rows where attempts > 2
print("Attempts > 2:")
print(df2[df2['attempts'] > 2], "\n")

# Question 2.6 - Count rows and columns
print("Shape of DataFrame:")
print("Rows:", df2.shape[0], " Columns:", df2.shape[1], "\n")

# Question 2.7 - Score between 15 and 20
print("Score between 15 and 20:")
print(df2[df2['score'].between(15, 20)], "\n")

# Question 2.8 - Attempts < 2 and Score > 15
print("Attempts < 2 AND Score > 15:")
print(df2[(df2['attempts'] < 2) & (df2['score'] > 15)], "\n")

# Question 2.9 - Change score in row 'd' to 11.5
df2.loc['d', 'score'] = 11.5
print("Updated Row 'd' Score to 11.5:")
print(df2, "\n")

# Question 2.10 - Mean of scores
print("Mean of Scores:")
print(df2['score'].mean(), "\n")

# Question 2.11 - Append and delete a new row
df2.loc['k'] = ['Ali', 18, 2, 'yes']
print("After Adding Row 'k':")
print(df2, "\n")
df2 = df2.drop('k')
print("After Deleting Row 'k':")
print(df2, "\n")

# Question 2.12 - Sort by 'name' (desc) and 'score' (asc)
print("Sorted DataFrame:")
print(df2.sort_values(by=['name','score'], ascending=[False,True]), "\n")

# Question 2.13 - Replace yes/no with True/False
df2['qualify'] = df2['qualify'].map({'yes':True, 'no':False})
print("Replaced Qualify Column:")
print(df2, "\n")

# Question 2.14 - Change 'James' to 'Suresh'
df2['name'] = df2['name'].replace('James', 'Suresh')
print("Updated Name 'James' to 'Suresh':")
print(df2, "\n")

# Question 2.15 - Delete 'attempts' column
df2 = df2.drop(columns=['attempts'])
print("Deleted 'attempts' Column:")
print(df2, "\n")

# Question 2.16 - Write to CSV with tab separator
df2.to_csv("dataframe.csv", sep='\t', index=True)
print("DataFrame written to 'dataframe.csv' with tab separator.\n")
