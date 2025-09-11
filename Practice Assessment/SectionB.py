import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, SimpleRNN, GRU, Dense, Dropout
from keras.metrics import Precision, Recall
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore') 

# Load Dataset
data = pd.read_csv('DataSets\AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)
passengers = data['#Passengers'].astype(float).values.reshape(-1, 1)

# Preprocessing
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(passengers)

# Sequencing and train test split
window_size = 12
x = []
y = []
target_dates = data.index[window_size:]

for i in range(window_size, len(scaled_data)):
    x.append(scaled_data[i - window_size:i, 0])
    y.append(scaled_data[i, 0])

x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test, dates_train, dates_test = train_test_split(
    x, y, target_dates, test_size=0.2, shuffle=False
)

x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

# Build Models

def build_rnn():
    model = Sequential()
    model.add(SimpleRNN(units=128, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(Dropout(0.2))
    model.add(SimpleRNN(units=128))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    return model

def build_lstm():
    model = Sequential()
    model.add(LSTM(units=128, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=128))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    return model

def build_gru():
    model = Sequential()
    model.add(GRU(units=128, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(Dropout(0.2))
    model.add(GRU(units=128))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    return model

# Training Function
def train_and_predict(model, name):
    METRICS = ['accuracy', Precision(name='precision'), Recall(name='recall')]
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=METRICS)

    print(f"\nTraining {name}...\n")
    history = model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=1)

    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions).flatten()
    actual = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

    rmse = np.sqrt(mean_squared_error(actual, predictions))
    print(f"{name} RMSE: {rmse:.4f}")

    return predictions, actual

# Run Models
rnn_pred, actual = train_and_predict(build_rnn(), "RNN")
lstm_pred, actual = train_and_predict(build_lstm(), "LSTM")
gru_pred, actual = train_and_predict(build_gru(), "GRU")

# Visualization
plt.figure(figsize=(13,7))
plt.plot(dates_test, actual, label='Actual Air Passengers', color='black', linewidth=2)
plt.plot(dates_test, rnn_pred, label='RNN Predictions', linestyle='--')
plt.plot(dates_test, lstm_pred, label='LSTM Predictions', linestyle='--')
plt.plot(dates_test, gru_pred, label='GRU Predictions', linestyle='--')

plt.title('Actual vs Predicted Air Passengers (RNN vs LSTM vs GRU)')
plt.xlabel('Date')
plt.ylabel('Air Passengers')
plt.legend()
plt.show()

""" Note:
RNN captured basic patterns but struggled with long-term trends.
LSTM performed better, handling long dependencies well.
GRU gave results close to LSTM, often faster and competitive."""