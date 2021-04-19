import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

df = pd.read_csv("Iris.csv")
print(df.head(10))
print(df.info())
print(df.columns)
print(df.tail(20))
print(df.isna().sum())
le = LabelEncoder()
df["Species"] = le.fit_transform(df["Species"])
df.info()
y = df["Species"]
X = df[["PetalLengthCm", "SepalWidthCm", "SepalLengthCm", "PetalWidthCm"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
# model = SVC(kernel="sigmoid")
# model = SVC(kernel="rbf")
model = SVC(kernel="poly", degree=2)
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, predicted))
