import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

wine = datasets.load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['type'] = pd.Series(wine.target)
# print("head", df.head())
# print(df.columns)
# print(set(df['type']))
y = df["type"]
X = df[["alcohol", "proanthocyanins", "proline"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))
