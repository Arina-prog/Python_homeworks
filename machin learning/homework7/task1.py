import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix

df = pd.read_csv("train.csv")
print("head", df.head(10))
print("column", df.columns)
print("tail", df.tail(20))
print("describe", df.describe())
print("isna", df.isna().sum())
df.info()
df.fillna(df.mean(), inplace=True)
print("isna", df.isna().sum())
y = df["four_g"]
X = df[["int_memory", "ram", "clock_speed", "price_range"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(metrics.accuracy_score(y_test, y_pred))