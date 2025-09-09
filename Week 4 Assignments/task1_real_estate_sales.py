import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv('DataSets\Real_Estate_Sales_2001-2022_GL-Short.csv', index_col="Serial Number")

print("Real Estate Dataset:\n", df.head())
print(df.info())
print(df.dtypes)
print(df.describe())
print("Shape:", df.shape)

x = df[["Assessed Value"]].values
y = df["Sale Amount"].values

plt.scatter(x, y)
plt.xlabel("Assessed Value")
plt.ylabel("Sale Amount")
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
print(f"{x_train.shape[0]} train / {x_test.shape[0]} test")

lr = LinearRegression()
lr.fit(x_train, y_train)

print("Intercept:", lr.intercept_)
print("Slope:", lr.coef_[0])

def predict_sale(assessed_value):
    return lr.coef_[0]*assessed_value + lr.intercept_

print("Sample Predictions:")
for val in x[:3]:
    print(predict_sale(val[0]))

y_pred = lr.predict(x_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
