import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv("annual-balance.csv")
print(df.head())
print(df.columns)
print(set(df["Status"]))
le = LabelEncoder()
status_encoded = le.fit_transform(df["Status"])
print(status_encoded)
values_encoded = le.fit_transform(df["Values"])
print(values_encoded)
instit_encoded = le.fit_transform(df["Institutional_sector_code"])
print(instit_encoded)
label = status_encoded
features = zip(values_encoded, instit_encoded)
model = GaussianNB()
model.fit(list(features), label)
print(model.predict([[5278, 10]]))
