import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

#load dataset
col_names = ['donor_id', 'name', 'email', 'password', 'contact_number', 'city', 'blood_group', 'availability' , 'months_since_first_donation', 'number_of_donation', 'pints_donated', 'created_at']
df = pd.read_csv(r'DataSets\blood_donor_dataset.csv', header=1, names=col_names, index_col='donor_id', parse_dates=['created_at'])

# Convert date into numeric feature
df['days_since_created'] = (df['created_at'] - df['created_at'].min()).dt.days

#x and y
feature_cols = ['blood_group', 'months_since_first_donation', 'number_of_donation', 'pints_donated', 'days_since_created' ]
x = df[feature_cols]
y = df['availability']

#encode categorical feature (blood_group)
x = pd.get_dummies(x, columns=['blood_group'], drop_first=True)

#preprocessing
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

#encode y
le = LabelEncoder()
y = le.fit_transform(y)

#split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size= 0.4, random_state=23)

#logistic regression
lr = LogisticRegression(max_iter=1000)

#train
lr = lr.fit(x_train, y_train)

#predict
y_pred = lr.predict(x_test)

#accuracy score
print('Accuracy Score: ', accuracy_score(y_test, y_pred))

#classification report
print('Classification Report:\n', classification_report(y_test, y_pred))

#confusion matrix
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))


