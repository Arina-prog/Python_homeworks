import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("business-price.csv")
# print(df.head())
# print(df.columns)
print(df)
y = df["Period"]
X = df[["Data_value"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
model = LinearRegression()
model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
