import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn import metrics


df_train = pd.read_csv("mnist_train.csv", header=None)
# print("info\n", df_train.info())
# print("head\n", df_train.head(2))
# print("columns\n", df_train.columns)
# print("columns\n", len(df_train.columns))
# print("Shape\n", df_train.shape)
# print("isna\n", df_train.isna().sum())
# print("tail\n", df_train.tail(3))
df_test = pd.read_csv("mnist_test.csv", header=None)
# print("Shape\n", df_test.shape)
# print(df_train.iloc[:, 0].value_counts())
sns.countplot(df_train.iloc[:, 0])
plt.show()
X_train = df_train.iloc[:, 1:]
y_train = df_train.iloc[:, 0]
X_test = df_test.iloc[:, 1:]
y_test = df_test.iloc[:, 0]
# print(X_train.iloc[0])
# print(X_train.iloc[0, :]),
# image1 = X_train.iloc[0].values.reshape(28, 28)
image2 = X_train.iloc[1000].values.reshape(28, 28)
plt.imshow(image2, cmap="gray")
plt.title(y_train.iloc[1000])
print(X_train.iloc[1000, 0])
plt.show()
model = SVC(kernel="rbf")
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, predicted))
# print(model.)