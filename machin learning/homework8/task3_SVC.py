import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("train.csv")
print("columns name\n ", df.columns)
# print("head fail\n", df.head())
# print("tail \n", df.tail(20))
# print("verlutsutyun \n", df.describe())
df.info()
print(df.isna().sum())
y = df["four_g"]
X = df.drop("four_g", axis=1)
# X = df[["dual_sim", "int_memory", "ram", "price_range"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = SVC(kernel="linear")
model.fit(X_train, y_train)
predicted = model.predict(X_test)
# print(predicted)
print("Accuracy:", metrics.accuracy_score(y_test, predicted))