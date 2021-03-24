import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

########### tvyalneri @ntrutyun######
df = pd.read_csv("diabetes.csv")

########### tvyalneri hetazotum########
print(df.columns)
# print(df.tail(20))

########## xndri dzevakerpum  ###########
y = df["Outcome"]
X = df[["BMI", "Glucose"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)

######### algoritmi @ntrutyun ev xndri lutsum########
model = GaussianNB()
model.fit(X_train, y_train)

#########lutsman voraki stugum########
y_pred = model.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

##########algoritmi kirarutyun#############



