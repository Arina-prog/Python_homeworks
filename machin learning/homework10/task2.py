import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import tree

df = pd.read_csv("annual-balance-sheets-and-accumulation-accounts-200817-provisional-csv.csv")
print(df.columns)
df.info()
le = LabelEncoder()
df["Institutional_sector_name"] = le.fit_transform(df["Institutional_sector_name"])
df["Descriptor"] = le.fit_transform(df["Descriptor"])
df["SNA08TRANS"] = le.fit_transform(df["SNA08TRANS"])
df["Asset_liability_code"] = le.fit_transform(df["Asset_liability_code"])
df["Status"] = le.fit_transform(df["Status"])
df["Values"] = le.fit_transform(df["Values"])
print(df.isna().sum())
df.info()
y = df["Status"]
X = df[["Values", "Asset_liability_code", "Descriptor"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = DecisionTreeClassifier(criterion="gini", max_depth=5)
# model = DecisionTreeClassifier(criterion="entropy", max_depth=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))
#
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=250)
fn = ["Values", "Asset_liability_code", "Descriptor"]
cn = ["positive", "negative"]
tree.plot_tree(model, feature_names=fn, class_names=cn, filled=True)
plt.show()
tree_representation = tree.export_text(model)
print(tree_representation)
