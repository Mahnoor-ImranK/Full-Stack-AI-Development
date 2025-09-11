import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
housing = fetch_california_housing()
x, y = housing.data, housing.target

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Model
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1) 
])

model.compile(optimizer='adam',
              loss='mse',
              metrics=['mae'])

# Training
history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, verbose=1)

# Evaluation
print("Evaluation:")
model.evaluate(x_test, y_test, verbose=1)
