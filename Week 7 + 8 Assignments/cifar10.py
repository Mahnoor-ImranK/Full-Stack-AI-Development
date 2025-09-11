import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

print ('x_train:', x_train.shape)
print ('x_test:', x_test.shape)

print ('x_train[0]:', x_train[0])

plt.figure(figsize=(12,2))
plt.imshow(x_train[9])
plt.show()

print('y_train:', y_train.shape)
print('y_train[:7]:', y_train[:7])

y_train = y_train.reshape(-1,)
print(y_train[:7])

classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def plot_sample(x, y, index):
    plt.figure(figsize=(12,2))
    plt.imshow(x[index])
    plt.xlabel(classes[y[index]])
    plt.show()

plot_sample(x_train, y_train, 0)

x_train = x_train/255
x_test = x_test/255

print('x_train:\n', x_train)
print('x_test:\n', x_test)

#model building and training
ann = models.Sequential([
    layers.Flatten(input_shape = (32, 32, 3)),
    layers.Dense(3000, activation = 'relu'),
    layers.Dense(1000, activation = 'relu'),
    layers.Dense(10, activation = 'softmax')
]) 

ann.compile(optimizer = 'SGD',
            loss = 'sparse_categorical_crossentropy',
            metrics = ['accuracy'])

print('Training:\n')
ann.fit(x_train, y_train, epochs = 4)

print('Evaluation:\n')
ann.evaluate(x_test, y_test)

from sklearn.metrics import confusion_matrix, classification_report
import numpy as np

y_pred = ann.predict(x_test)
y_pred_classes = [np.argmax(element) for element in y_pred]

print('Classification Report:\n', classification_report(y_test, y_pred_classes))

#cnn
cnn = models.Sequential([
    layers.Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu', input_shape = (32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(filters = 64, kernel_size = (3, 3), activation = 'relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation = 'relu'),
    layers.Dense(10, activation = 'softmax')   #softmax normalize probability
]) 

cnn.compile(optimizer = 'adam',
            loss = 'sparse_categorical_crossentropy',
            metrics = ['accuracy'])

print('Training:\n')
cnn.fit(x_train, y_train, epochs = 4)

print('Evaluation:\n')
cnn.evaluate(x_test, y_test)

y_test = y_test.reshape(-1,)
plot_sample(x_test, y_test, 0)

print('y_test[:7]:', y_test[:7])

y_pred = cnn.predict(x_test)
y_pred_classes = [np.argmax(element) for element in y_pred]

print('y_pred_classes[:7]:', y_pred[:7])

print('Classification Report:\n', classification_report(y_test, y_pred_classes))
