# * Implement regression task with several input features (X-s_ using LinearRegression model
# Реализовать задачу регрессии с несколькими входными функциями (X-s_ с использованием модели LinearRegression

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

previous_value = np.array([2, 4, 8, 16, 32, 64])
next_value = np.array([4, 8, 16, 32, 64, 128])
previous_value = previous_value.reshape(-1, 1)
plt.scatter(previous_value,next_value, color='red')
plt.xlabel("previous_value")
plt.ylabel("next_value")
# plt.show()
model = LinearRegression()
model.fit(previous_value, next_value)
model.intercept_
model.coef_
plt.plot(previous_value, model.predict(previous_value))
plt.show()
y_pred = model.predict([[int(input("input value "))]])
print(y_pred)
print(model.score(previous_value, next_value))
