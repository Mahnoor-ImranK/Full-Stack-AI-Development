import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

dataset = load_iris()
df = pd.DataFrame(dataset.data, columns= dataset.feature_names)
df['target'] = dataset.target

print('Iris Dataset: \n', df)

#fifth column
print(df['target'].unique())

#shape
print(df.shape)

#no. of 0 and 1
print(df['target'].value_counts())

#percentage of data
print(df['target'].value_counts(normalize=True))

#plotting
df['target'].plot.hist()
plt.show()

#statistical measurements and transpose
print(df.describe().T)

feature_cols = dataset.feature_names
x = df[feature_cols]
y = df['target']

#plot each feature
for col in df[feature_cols]:
    plt.title(col)
    df[col].plot.hist()
    plt.show()

sns.pairplot(df, hue = 'target')
plt.show()

#separate target and features
y = df['target']
x = df.drop('target', axis=1)

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#no. of samples separated for train and test
x_train_samples = x_train.shape[0]
x_test_samples = x_test.shape[0]
print(f'{x_train_samples} for training and {x_test_samples} for testing' )

#svc
svc = SVC(kernel='linear')

#train
svc.fit(x_train, y_train)

#predict
y_pred = svc.predict(x_test)

#accuracy score
print('Accuracy Score: ', accuracy_score(y_test, y_pred))

#classification report
print('Classification Report: \n', classification_report(y_test, y_pred))

#confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d').set_title('Confusion Matrix of Linear SVC')
plt.show()
