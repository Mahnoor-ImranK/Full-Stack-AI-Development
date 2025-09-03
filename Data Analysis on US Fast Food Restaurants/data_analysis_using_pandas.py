import pandas as pd

df = pd.read_csv('DataSets\FastFoodRestaurants.csv')

print(df)
print("df - data types:\n", df.dtypes)
print("df.info():")
print(df.info())

print('Last three Rows:')
print(df.tail(3))

print('First Three Rows:')
print(df.head(3))

print("Summary Statistics:\n", df.describe())
print("Shape (rows, cols):", df.shape)

col = df['province']
print("Single column:\n", col)

mul_cols = df[['province', 'city']]
print("Multiple columns:\n", mul_cols)

print("Single row using .loc:\n", df.loc[1])
print("Multiple rows using .loc:\n", df.loc[[1, 3]])
print("Slice of rows using .loc:\n", df.loc[1:5])
print("Conditional selection:\n", df.loc[df['province'] == 'CA'])
print("Single column with .loc:\n", df.loc[:1, 'province'])
print("Multiple columns with .loc:\n", df.loc[:1, ['province', 'city']])
print("Slice of columns with .loc:\n", df.loc[:1, 'city':'longitude'])
print("Conditional row & col selection:\n", df.loc[df['province'] == 'CA', 'city':'longitude'])

df_index_col = pd.read_csv(
    'DataSets\FastFoodRestaurants.csv',
    index_col='address'
)

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

print("Single row using .iloc:\n", df_index_col.iloc[0])
print("Multiple rows using .iloc:\n", df_index_col.iloc[[1, 3]])
print("Slice of rows using .iloc:\n", df_index_col.iloc[1:4])
print("Conditional selection using .loc:\n", df_index_col.loc[df_index_col['province'] == 'CA'])
print("Single column using .iloc:\n", df_index_col.iloc[:, 0])
print("Multiple columns using .iloc:\n", df_index_col.iloc[:, [0, 1]])
print("Slice of columns using .iloc:\n", df_index_col.iloc[:, 0:2])
print("Combined selection using .iloc:\n", df_index_col.iloc[[1, 3], 0:2])

print("Single row using .iloc:\n", df_index_col.iloc[0])
print("Multiple rows using .iloc:\n", df_index_col.iloc[[1, 3, 5]])
print("Slice of rows using .iloc:\n", df_index_col.iloc[2:5])
print("Single column using .iloc:\n", df_index_col.iloc[:, 2])
print("Multiple columns using .iloc:\n", df_index_col.iloc[:, [2, 4]])
print("Slice of columns using .iloc:\n", df_index_col.iloc[:, 2:4])
print("Combined selection using .iloc:\n", df_index_col.iloc[[1, 3, 5], 2:4])

print("Next Run")

df.loc[len(df.index)] = [
    '123 New Street',
    'Lahore',
    'Pakistan',
    'burger,new',
    31.5204,
    74.3587,
    'New FastFood',
    '54000',
    'Punjab',
    'www.newfastfood.pk'
]
print("After adding new row:\n", df)

df.drop([1, 2, 3, 5], axis=0, inplace=True)
print("After removing rows:\n", df)

df.rename(columns={'postalCode': 'zip_code', 'latitude': 'lat', 'longitude': 'lng'}, inplace=True)
print("After renaming columns:\n", df)

df.drop(['address', 'name', 'city', 'province'], axis=1, inplace=True)
print("After dropping columns:\n", df)

df.rename(index={0: 7, 1: 10, 2: 100}, inplace=True)
print("After renaming rows:\n", df)

selected_rows = df.query('lat > 40 or zip_code == "90210"')
print(selected_rows.to_string())
print(len(selected_rows))

sorted_df = df.sort_values(by='lat')
print(sorted_df.to_string(index=False))

df1 = df.sort_values(by=['zip_code', 'lat'])
print("Sorting by zip_code (ascending) and then by lat (ascending):\n")
print(df1.to_string(index=False))
