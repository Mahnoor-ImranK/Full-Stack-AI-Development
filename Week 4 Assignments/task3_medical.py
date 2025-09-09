import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

#load dataset
df = pd.read_csv(
    r"DataSets\number-of-registered-medical-and-dental-doctors-by-gender-in-pakistan (1).csv",
    index_col="Years"
)

df["Female Doctors"] = df["Female Doctors"].str.replace(",", "").astype(float)
df["Female Dentists"] = df["Female Dentists"].str.replace(",", "").astype(float)

print(df.head())
print(df.info())
print("Shape:", df.shape)

#features and target
x = df[["Female Doctors"]].values
y = df["Female Dentists"].values

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print(f"{x_train.shape[0]} train / {x_test.shape[0]} test")

#train
lr = LinearRegression()
lr.fit(x_train, y_train)

print("Intercept:", lr.intercept_)
print("Slope:", lr.coef_[0])

#predict
def predict_dentists(female_doctors):
    return lr.coef_[0]*female_doctors + lr.intercept_

print("Sample Predictions:")
for val in x[:3]:
    print(predict_dentists(val[0]))

#model evaluation
y_pred = lr.predict(x_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
