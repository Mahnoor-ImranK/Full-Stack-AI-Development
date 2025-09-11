import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from keras.metrics import Precision, Recall
from sklearn.metrics import mean_squared_error

#load dataset
data = pd.read_csv('DataSets\AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)
passengers = data['#Passengers'].astype(float).values.reshape(-1, 1)

#preprocessing
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(passengers)

#sequencing and train test split
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
    x, y, target_dates, test_size= 0.2, shuffle=False
)

x_train = x_train.reshape((x_train.shape[0], x_train.shape[1],1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1],1))

#build lstm model
model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(1))

METRICS = metrics = ['accuracy', Precision(name='precision'), Recall(name='recall')]
model.compile(optimizer='adam', loss='mean_squared_error', metrics = METRICS)

#training and model evaluation
history = model.fit(x_train, y_train, epochs=100, batch_size=32, validation_split=0.1)

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions).flatten()
y_test = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

print('RMSE: ', np.sqrt(mean_squared_error(y_test, predictions)))

#visualize model performance
plt.figure(figsize=(13,7))
plt.plot(dates_test, y_test, label='Actual Air Passengers')
plt.plot(dates_test, predictions, label='Predicted Air Passengers')
plt.title('Actual vs Predicted Air Passengers')
plt.xlabel('Date')
plt.ylabel('Air Passengers')
plt.legend()
plt.show()