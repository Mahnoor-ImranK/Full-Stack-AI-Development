import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.preprocessing import LabelEncoder

#load dataset
col_names = ['age', 'sex', 'bp', 'cholesterol', 'na_to_k', 'drug']
df = pd.read_csv('DataSets\go_decision_data.csv', header=1, names=col_names)

# Encode categorical variables
le_sex = LabelEncoder()
le_bp = LabelEncoder()
le_chol = LabelEncoder()
le_drug = LabelEncoder()

df['sex'] = le_sex.fit_transform(df['sex'])
df['bp'] = le_bp.fit_transform(df['bp'])
df['cholesterol'] = le_chol.fit_transform(df['cholesterol'])
df['drug'] = le_drug.fit_transform(df['drug'])

# Split dataset
feature_cols = ['age', 'sex', 'bp', 'cholesterol', 'na_to_k']
x = df[feature_cols]
y = df['drug']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

#decision tree classifier
dtc = DecisionTreeClassifier()

#train
dtc = dtc.fit(x_train, y_train)

#predict
y_pred = dtc.predict(x_test)

#accuracy
print('Accuracy Score: ', metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report

#classification report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(dtc, out_file=dot_data, filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols,
                class_names= le_drug.classes_
                )
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('drug.png')
Image(graph.create_png())

#create dtc object
dtc = DecisionTreeClassifier(criterion='entropy', max_depth=3)

#train
dtc = dtc.fit(x_train, y_train)

#predict
y_pred = dtc.predict(x_test)

#accuracy
print('Accuracy Score: ', metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(dtc, out_file=dot_data, filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols,
                class_names=le_drug.classes_
                )
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('drug2.png')
Image(graph.create_png())

#classification report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
