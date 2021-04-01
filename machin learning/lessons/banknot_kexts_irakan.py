import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics


df = pd.read_csv("bill_authentication.csv")
print("columns name\n ", df.columns)
print("head fail\n", df.head())
print("tail \n", df.tail(20))
print("verlutsutyun \n", df.describe())
df.info()
# print(df.isna())
print(df.isna().sum())
y = df["Class"]
##########bolor syunern baci Classic vercnel vorpes X
X = df.drop("Class", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = SVC(kernel="linear")
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, predicted))
