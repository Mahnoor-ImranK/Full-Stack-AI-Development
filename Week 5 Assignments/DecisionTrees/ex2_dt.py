import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

#load dataset
col_names = ['age', 'experience', 'rank', 'nationality', 'go']
df = pd.read_csv('G:\FULLSTACK-AI-BOOTCAMP-B2-MonTOFri-7TO9-PM-Explorer\DecisionTrees\go_decision_data.csv', header=1, names=col_names)

#encode
le_nationality = LabelEncoder()
le_go = LabelEncoder()

df['nationality'] = le_nationality.fit_transform(df['nationality'])
df['go'] = le_go.fit_transform(df['go'])

#split
feature_cols = ['age', 'experience', 'rank', 'nationality']
x = df[feature_cols]
y = df['go']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=24)

#dtc
dtc = DecisionTreeClassifier()

#train
dtc = dtc.fit(x_train, y_train)

#predict
y_pred = dtc.predict(x_test)

#accuracy
print('Accuracy Score: ', metrics.accuracy_score(y_test, y_pred))

#classification  report
print('Classification Report: \n')
print(classification_report(y_test, y_pred))
                                      
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(dtc, out_file=dot_data, filled= True, rounded= True,
                special_characters= True, feature_names= feature_cols,
                class_names= le_go.classes_)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('go.png')
Image(graph.create_png())

#entropy
dtc = DecisionTreeClassifier(criterion= 'entropy', max_depth= 4)

#train
dtc = dtc.fit(x_train, y_train)

#predict
y_pred = dtc.predict(x_test)

#accuracy
print('Accuracy Score: ', metrics.accuracy_score(y_test, y_pred))

#classification  report
print('Classification Report: \n')
print(classification_report(y_test, y_pred))

dot_data = StringIO()
export_graphviz(dtc, out_file=dot_data, filled= True, rounded= True,
                special_characters= True, feature_names= feature_cols,
                class_names= le_go.classes_)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('go2.png')
Image(graph.create_png())

