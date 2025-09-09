import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

#load dataset
df = pd.read_csv(r"DataSets\50_Startups (1).csv")

print(df.head())
print(df.info())
print(df.dtypes)
print(df.describe())
print("Shape:", df.shape)

#encode categorical column
df = pd.get_dummies(df, drop_first=True)   

#features and target
x = df.drop("Profit", axis=1).values
y = df["Profit"].values

#correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
print(f"{x_train.shape[0]} train / {x_test.shape[0]} test")

#train
lr = LinearRegression()
lr.fit(x_train, y_train)

print("Intercept:", lr.intercept_)
print("Slope:", lr.coef_)

#predict
y_pred = lr.predict(x_test)

#model evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
