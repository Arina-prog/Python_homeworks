import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("us-counties.csv")
print("head", df.head(4))
print("tail", df.tail(2))
print("columns", df.columns)
print("shape", df.shape)
print(df.info())
print("isna", df.isna().sum())
# rand = RandomForestClassifier(n_estimators=86, criterion="gini")
# df.hist()
# sns.countplot()
# plt.matshow(df.corr())

# plt.show()
X = df[["date", "fips"]]
y = df["deaths"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101, stratify=y)

df[["fips"]].fillna(value=1, inplace=True)
df[["date"]].fillna(value=1, inplace=True)
print(X.info())
print(y.info())
# print(help(df.fillna))
