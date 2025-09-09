import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

#load dataset
df = pd.read_csv(r"DataSets\housing.csv")

#missing values
df = df.dropna()

#encode categorical column
df = pd.get_dummies(df, drop_first=True)   

x = df.drop(columns=["median_house_value"])
y = df["median_house_value"]

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

#train
lr = LinearRegression()
lr.fit(x_train, y_train)

#predict
y_pred = lr.predict(x_test)

#model evaluation
print("Intercept:", lr.intercept_)
print("Coefficients:", lr.coef_)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
