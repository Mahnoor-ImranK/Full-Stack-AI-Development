import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from six import StringIO
from IPython.display import Image
import pydotplus

#load iris
dataset = load_iris()
df = pd.DataFrame(dataset.data, columns= dataset.feature_names)
df['target'] = dataset.target

print('Iris Dataset: \n', df)

feature_cols = dataset.feature_names
x = df[feature_cols]
y = df['target']

#split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state= 42)

#dtc
dtc= DecisionTreeClassifier()

#train
dtc = dtc.fit(x_train, y_train)

#predict
y_pred = dtc.predict(x_test)

#accuracy score
print('Accuracy Score: ', accuracy_score(y_test, y_pred))

#classification report
print('Classification Report: \n', classification_report(y_test, y_pred))

dot_data = StringIO()
export_graphviz(dtc, out_file= dot_data, filled= True, rounded= True,
                special_characters= True, feature_names= feature_cols,
                class_names= dataset.target_names)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('iris.png')
Image(graph.create_png())

#entropy
dtc = DecisionTreeClassifier(criterion= 'entropy', max_depth= 4)

#train
dtc = dtc.fit(x_train, y_train)

#predict
y_pred = dtc.predict(x_test)

#accuracy score
print('Accuracy Score: ', accuracy_score(y_test, y_pred))

#classification report
print('Classification Report: \n', classification_report(y_test, y_pred))

dot_data = StringIO()
export_graphviz(dtc, out_file= dot_data, filled= True, rounded= True,
                special_characters= True, feature_names= feature_cols,
                class_names= dataset.target_names)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('iris2.png')
Image(graph.create_png())
