import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_excel("car_data1.xlsx")
print(df.columns)
# print(df.tail(10))
# print(df.head(8))
# print(df.shape)
le =LabelEncoder()
df["buying"] = le.fit_transform(df["buying"])
df["maint"] = le.fit_transform(df["maint"])
df["class"] = le.fit_transform(df["class"])
df["safety"] = le.fit_transform(df["safety"])
X = df[["maint", "class","safety"]]
y = df["buying"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = GaussianNB()
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print(metrics.accuracy_score(y_test, predicted))
