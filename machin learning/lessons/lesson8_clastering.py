import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df = pd.read_csv("train.csv")
print(df.columns)
# print(df.head(10))
# print("tpel fayli verjic\n",df.tail(10))
# print("nkaragrakan statistika\n", df.describe())

#####stugel bacakayox arzheqneri tipern ev anhrazheshtutyan depqum konvertacnel############
print("info konvertaciayic araj",)
df.info()
print("\n")
le = LabelEncoder()
df["Name"] = le.fit_transform(df["Name"])
df["Sex"] = le.fit_transform(df["Sex"])
df["Ticket"] = le.fit_transform(df["Ticket"])
df["Cabin"] = le.fit_transform(df["Cabin"])
df["Embarked"] = le.fit_transform(df["Embarked"])
print("info konvertaciayic heto")
df.info()
#########stugel bacakayox arzheqnern ev lracnel###########
print("bacakayox arzheqneri qanak", df.isna().sum())
# print(df["Age"])
df.fillna(df.mean(), inplace=True)
# df.fillna(0, inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
# print(df["Age"])
print("\nbacakayox arzheqneri qanak lracneluc heto", df.isna().sum())

X = df[["Sex", "Ticket", "Pclass", "Age"]]
model = KMeans(n_clusters=3)
model.fit(X)
print(model.predict(X))