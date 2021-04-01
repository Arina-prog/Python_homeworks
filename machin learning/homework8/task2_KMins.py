import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("train.csv")
print("columns name", df.columns)
print("tail", df.tail(10))
print("head", df.head(8))
print("shape", df.shape)
print("isna", df.isna().sum())
print("info", df.info())

X = df[["battery_power", "clock_speed", "four_g", "int_memory"]]
model = KMeans(n_clusters=3)
model.fit(X)
print(model.predict(X))