import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

df = pd.read_csv("BostonHousing.csv")
print(df.columns)
df.info()
print(df.isna().sum())
print(df.shape)
print(df.describe)
plt.matshow(df.corr())
plt.xticks(range(df.shape[1]), df.columns, fontsize=12, rotation=90)
plt.yticks(range(df.shape[1]), df.columns, fontsize=12)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=12)
df.hist()
plt.show()
y = df["tax"]
X = df[["rad", "nox", "zn"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = RandomForestClassifier(n_estimators=93)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_pred, y_test))
feature_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print(feature_imp)
