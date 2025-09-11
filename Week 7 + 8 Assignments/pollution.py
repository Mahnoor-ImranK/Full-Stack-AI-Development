import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import warnings
warnings.filterwarnings('ignore') 

# Load Dataset
df = pd.read_csv("DataSets\south-korean-pollution-data.csv")  
print(df.head())
print(df.columns)

# Features & Target 
target_col = "pm25"

# Drop non-numeric columns and target column from features
X = df.drop(columns=["date", "City", "District", "Country", target_col]).values
y = df[target_col].values

# Preprocessing
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

#split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Reshape
x_train = x_train.reshape((x_train.shape[0], 1, x_train.shape[1]))
x_test = x_test.reshape((x_test.shape[0], 1, x_test.shape[1]))

print("Train shape:", x_train.shape, y_train.shape)
print("Test shape:", x_test.shape, y_test.shape)

#rnn
def build_rnn():
    model = models.Sequential([
        layers.SimpleRNN(64, activation='relu', input_shape=(x_train.shape[1], x_train.shape[2])),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])
    return model

#lstm
def build_lstm():
    model = models.Sequential([
        layers.LSTM(64, activation='relu', input_shape=(x_train.shape[1], x_train.shape[2])),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])
    return model

#gru
def build_gru():
    model = models.Sequential([
        layers.GRU(64, activation='relu', input_shape=(x_train.shape[1], x_train.shape[2])),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])
    return model

# Training & Evaluation

def train_and_evaluate(model, name):
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    print(f"\nTraining {name}:\n")
    history = model.fit(x_train, y_train, epochs=10, batch_size=32,
                        validation_split=0.2, verbose=1)

    print(f"\nEvaluation {name}:\n")
    loss, mae = model.evaluate(x_test, y_test, verbose=1)
    
    # Predict
    y_pred = model.predict(x_test)
    
    # Evaluation metrics
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"{name} - Test MSE: {loss:.4f}, MAE: {mae:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}")

    return model, history, y_pred   

rnn_model, rnn_hist, rnn_pred = train_and_evaluate(build_rnn(), "SimpleRNN")   
lstm_model, lstm_hist, lstm_pred = train_and_evaluate(build_lstm(), "LSTM")   
gru_model, gru_hist, gru_pred = train_and_evaluate(build_gru(), "GRU")         

#graph
plt.figure(figsize=(12,6))
plt.plot(y_test[:100], label="Actual", color="black", linewidth=2)  
plt.plot(rnn_pred[:100], label="RNN Predicted", linestyle="--")
plt.plot(lstm_pred[:100], label="LSTM Predicted", linestyle="--")
plt.plot(gru_pred[:100], label="GRU Predicted", linestyle="--")

plt.title("Comparison of Actual vs Predicted Pollution Levels")
plt.xlabel("Sample Index")
plt.ylabel("PM2.5 Value")
plt.legend()
plt.show()
