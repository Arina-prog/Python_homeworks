import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("BostonHousing.csv")
y = df["tax"]
X = df[["rm", "medv", "nox"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = LinearRegression()
model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
print(model.predict([[23.12, 12, 0.51]]))
print(model.predict([[23.12, 12, 0.1]]))
print(model.predict([[24.12, 26, 0.1]]))
# print(accuracy_score(y_pred, y_test))
# print(mean_squared_error(y_test, y_pred))
