import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

previous_days = np.array([1, 7, 11, 21, 25, 28])
next_days = np.array([7, 11, 21, 25, 28, 31])
previous_days = previous_days.reshape(-1, 1)
# miachapanin darcnuma erkchapani reshape
# orinakneri grafik
# plt.scatter(previous_days,next_days )
# plt.xlabel("previous_days")
# plt.ylabel("next_days ")
# plt.show()
# print(previous_days)
ml_model = LinearRegression()
# superviz
ml_model.fit(previous_days, next_days)

ml_model.intercept_
#intercept
ml_model.coef_
#slope
# plt.scatter(previous_days,next_days , color='red')
# plt.xlabel('previous_days')
# plt.ylabel('next_days ')
# plt.plot(previous_days, ml_model.predict(previous_days))
# plt.show()
y_pred = ml_model.predict([[1]])
print(y_pred)
# print(help(ml_model.predict))