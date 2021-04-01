import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df = pd.read_csv("../homework8/melb_data.csv")
print("columns name", df.columns)
print("tail", df.tail(10))
print("head", df.head(8))
print("shape", df.shape)
print("isna", df.isna().sum())
print("info", df.info())
le = LabelEncoder()
df["Suburb"] = le.fit_transform(df["Suburb"])
df["Address"] = le.fit_transform(df["Address"])
df["Type"] = le.fit_transform(df["Type"])
df["Method"] = le.fit_transform(df["Method"])
df["SellerG"] = le.fit_transform(df["SellerG"])
df["Date"] = le.fit_transform(df["Date"])
df["CouncilArea"] = le.fit_transform(df["CouncilArea"])
df["Regionname"] = le.fit_transform(df["Regionname"])
df.info()
df.fillna(df.mean(), inplace=True)
X = df[["Address", "Price", "Distance"]]
model = KMeans(n_clusters=3)
model.fit(X)
print(model.predict(X))