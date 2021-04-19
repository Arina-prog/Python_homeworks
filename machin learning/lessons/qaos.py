import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

data = pd.read_csv("diabetes_csv.csv")

print(data.columns)
print(data.shape)
# print(data.head(3))
# print(data.tail(5))
# print(data.info())
# print(data.isna().sum())
y = data["class"]
X = data[["insu", "mass", "plas"]]

le = LabelEncoder()
y = le.fit_transform(y)
print(y[1:5])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

model = DecisionTreeClassifier(criterion="entropy", max_depth=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=240)

fn = ["insu", "mass", "plas"]
cn = ["positive", "negative"]

tree.plot_tree(model, feature_names=fn, class_names=cn, filled=True)
plt.show()

text_representation = tree.export_text(model)
print(text_representation)
