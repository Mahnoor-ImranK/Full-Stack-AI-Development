# Regression with Diabetes Dataset
# Models: Linear, Decision Tree, Random Forest,
#         Gradient Boosting, AdaBoost

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Regression models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor

#Load Dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

print("Shape of features:", X.shape)
print("Shape of target:", y.shape)

#Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Preprocessing
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "AdaBoost": AdaBoostRegressor(n_estimators=100, random_state=42)
}

#Train & Evaluate Models
results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results.append([name, mse, r2])
    print(f"{name}: MSE={mse:.2f}, R2={r2:.2f}")

#Store results in DataFrame
results_df = pd.DataFrame(results, columns=["Model", "MSE", "R2_Score"])
print("\n=== Model Comparison ===")
print(results_df)

#Graphs
plt.figure(figsize=(8, 5))
plt.barh(results_df["Model"], results_df["R2_Score"], color="skyblue")
plt.xlabel("R² Score")
plt.title("Comparison of Regression Models on Diabetes Dataset")
plt.show()
