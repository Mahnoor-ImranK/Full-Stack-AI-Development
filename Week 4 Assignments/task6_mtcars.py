import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

#load dataset
df = pd.read_csv(r"DataSets\mtcars.csv")

#drop non-numeric columns
df = df.drop(columns=["model"])

X = df.drop(columns=["mpg"])   
y = df["mpg"]                  

#split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

#train
lr = LinearRegression()
lr.fit(X_train, y_train)

print("Intercept:", lr.intercept_)
print("Coefficients:", lr.coef_)

#predict
y_pred = lr.predict(X_test)

#model evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
