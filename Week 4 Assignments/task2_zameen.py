import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv(
    r"DataSets\zameencom-property-data-By-Kaggle-Short.csv",
    delimiter=";",
    index_col="property_id"   
)

print("Columns:", df.columns.tolist())
print(df.head())
print(df.info())
print(df.describe())
print("Shape:", df.shape)

x = df[["bedrooms"]].values
y = df["price"].values

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
print(f"{x_train.shape[0]} train / {x_test.shape[0]} test")

#train
lr = LinearRegression()
lr.fit(x_train, y_train)

print("Intercept:", lr.intercept_)
print("Slope:", lr.coef_[0])

#predict
def predict_price(bedrooms):
    return lr.coef_[0]*bedrooms + lr.intercept_

print("Sample Predictions:")
for val in x[:3]:
    print(predict_price(val[0]))

#model evaluation
y_pred = lr.predict(x_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
