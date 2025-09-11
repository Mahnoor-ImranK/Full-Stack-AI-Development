import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy import stats
import statsmodels.api as sm

df = pd.read_csv(r'DataSets\us_house_Sales_data.csv', delimiter=',', index_col='MLS ID')
print('Data Types:\n', df.dtypes)
print('Data:\n', df.head(30))
print('Shape:\n', df.shape)

# Remove non-numeric characters
df['Bedrooms'] = df['Bedrooms'].astype(str).str.replace('[^\d.]', '', regex=True)
df['Bathrooms'] = df['Bathrooms'].astype(str).str.replace('[^\d.]', '', regex=True)
df['Area (Sqft)'] = df['Area (Sqft)'].astype(str).str.replace('[^\d.]', '', regex=True)
df['Price'] = df['Price'].astype(str).str.replace('[^\d.]', '', regex=True)

# Convert cleaned values to numeric
df['Area (Sqft)'] = pd.to_numeric(df['Area (Sqft)'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

df.dropna(subset=['Bedrooms', 'Price'], inplace=True)
df.dropna(subset=['Bathrooms', 'Price'], inplace=True)
df.dropna(subset=['Area (Sqft)', 'Price'], inplace=True)

sns.set_theme(style='whitegrid') #set theme

"""# sns.scatterplot(data= df, x='Bedrooms', y='Price')
# plt.show()

# sns.scatterplot(data= df, x='Bathrooms', y='Price')
# plt.show()"""

sns.regplot(data= df, x='Area (Sqft)', y='Price', line_kws={'color': 'red'})
plt.show()

sns.lmplot(data= df, x='Area (Sqft)', y='Price', line_kws={'color': 'red'})
plt.show()


"""# sns.regplot(data= df, x='Year Built', y='Price')
# plt.show()

# sns.regplot(data= df, x='Property Type', y='Price')
# plt.show()"""

#outliers detection

numeric_df = df.select_dtypes(include=[np.number]) # Select only numeric columns

z_scores = np.abs(stats.zscore(numeric_df))
outlier = df[(z_scores<3).all(axis = 1)]

#graph
sns.regplot(data= outlier, x='Area (Sqft)', y='Price', line_kws={'color': 'red'})
plt.show()

sns.lmplot(data= outlier, x='Area (Sqft)', y='Price', line_kws={'color': 'red'})
plt.show()


#correlations
corr_matrix= df.corr(numeric_only=True)
print('Correlations:\n', corr_matrix)
plt.figure(figsize=(9,7))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heat map of US House Sales Data')
plt.show()

#x and y values
x = df[['Area (Sqft)', 'Bedrooms', 'Bathrooms']]
y = df['Price']

#preprocessing
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

#split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.3, random_state=20)

#linear regression
lr = LinearRegression()

#train
lr = lr.fit(x_train, y_train)

#intercept
print('Intercept: ', lr.intercept_)

#coefficient
print('Coefficient: ', lr.coef_)

#predict
y_pred = lr.predict(x_test)

result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted:\n" , result)

#evaluation metrics
print('R2 Score: ', r2_score(y_test, y_pred))
print('MSE: ', mean_squared_error(y_test, y_pred))
print('MAE: ', mean_absolute_error(y_test, y_pred))
print ('RMSE: ', np.sqrt(mean_squared_error(y_test, y_pred)))

#statistical summary
x_sm = sm.add_constant(x_scaled)
ols = sm.OLS(y,x_sm).fit()
print('Statistical Summary:\n', ols.summary())


"""Linear Regression model is not suitable for this dataset.
 According to my analysis there is relation between Area and Price. 
 The model doesn't predict the values accurately."""