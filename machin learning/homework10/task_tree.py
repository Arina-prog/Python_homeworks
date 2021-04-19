import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

df=pd.read_csv("bill_authentication.csv")
print("columns\n", df.columns)
# print("head\n", df.head(5))
# print("tail\n", df.tail(3))
print("shape\n", df.shape)
print(df.isna().sum())
# print("info\n")
df.info()
y = df["Class"]
X = df[["Variance", "Entropy", "Curtosis"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
# model = DecisionTreeClassifier(criterion="entropy", max_depth=5)
model = DecisionTreeClassifier(criterion="gini", max_depth=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_test))
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4,4), dpi=300)
fn = ["Variance", "Entropy", "Curtosis"]
cn = ["positive", "negative"]
tree.plot_tree(model, feature_names=fn, class_names=cn, filled=True)
plt.show()
tree_representation = tree.export_text(model)
print(tree_representation)
