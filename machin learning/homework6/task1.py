import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn import metrics

df = pd.read_csv("diabetes.csv")
y = df["Outcome"]
X = df[["BMI", "Glucose", "BloodPressure"]]
print(df.columns)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
y_pred = logmodel.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(metrics.accuracy_score(y_test, y_pred))