import pandas as pd

df = pd.read_csv('G:\\FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer\\DataSetForPractice\\startup_growth_investment_data.csv')

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

col = df['Country']
print("Single column:\n", col)

mul_cols = df[['Country', 'Industry']]
print("Multiple columns:\n", mul_cols)

print("Single row using .loc:\n", df.loc[1])
print("Multiple rows using .loc:\n", df.loc[[1, 3]])
print("Slice of rows using .loc:\n", df.loc[1:5])
print("Conditional selection:\n", df.loc[df['Country'] == 'USA'])
print("Single column with .loc:\n", df.loc[:1, 'Country'])
print("Multiple columns with .loc:\n", df.loc[:1, ['Country', 'Industry']])
print("Slice of columns with .loc:\n", df.loc[:1, 'Industry':'Growth Rate (%)'])
print("Conditional row & col selection:\n", df.loc[df['Country'] == 'USA', 'Industry':'Growth Rate (%)'])

df_index_col = pd.read_csv(
    'G:\\FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer\\DataSetForPractice\\startup_growth_investment_data.csv',
    index_col='Startup Name'
)

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

print("Single row using .iloc:\n", df_index_col.iloc[0])
print("Multiple rows using .iloc:\n", df_index_col.iloc[[1, 3]])
print("Slice of rows using .iloc:\n", df_index_col.iloc[1:4])
print("Conditional selection using .loc:\n", df_index_col.loc[df_index_col['Country'] == 'USA'])
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
    'New AI Startup',
    'AI',
    3,
    7500000,
    25000000,
    5,
    'Pakistan',
    2023,
    45.0
]
print("After adding new row:\n", df)

df.drop([1, 2, 3, 5], axis=0, inplace=True)
print("After removing rows:\n", df)

df.rename(columns={
    'Investment Amount (USD)': 'InvestmentUSD',
    'Valuation (USD)': 'ValuationUSD',
    'Growth Rate (%)': 'GrowthRate'
}, inplace=True)
print("After renaming columns:\n", df)

df.drop(['Startup Name', 'Industry', 'Country'], axis=1, inplace=True)
print("After dropping columns:\n", df)

df.rename(index={0: 7, 1: 10, 2: 100}, inplace=True)
print("After renaming rows:\n", df)

selected_rows = df.query('GrowthRate > 40 or InvestmentUSD > 10000000')
print(selected_rows.to_string())
print(len(selected_rows))

sorted_df = df.sort_values(by='GrowthRate')
print(sorted_df.to_string(index=False))

df1 = df.sort_values(by=['InvestmentUSD', 'GrowthRate'])
print("Sorting by InvestmentUSD (ascending) and then by GrowthRate (ascending):\n")
print(df1.to_string(index=False))
