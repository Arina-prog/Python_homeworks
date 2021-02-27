import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

naxord_orer = np.array([1, 7, 11, 21, 25, 28])
hajord_orer = np.array([7, 11, 21, 25, 28, 31])
naxord_orer = naxord_orer.reshape(-1, 1)
# miachapanin darcnuma erkchapani reshape
# orinakneri grafik
# plt.scatter(naxord_orer,hajord_orer)
# plt.xlabel("naxord_orer")
# plt.ylabel("hajord_orer")
# plt.show()
# print(naxord_orer)
ml_model = LinearRegression()
# superviz
ml_model.fit(naxord_orer, hajord_orer)

ml_model.intercept_
#intercept
ml_model.coef_
#slope
# plt.scatter(naxord_orer,hajord_orer, color='red')
# plt.xlabel('naxord_orer')
# plt.ylabel('hajord_orer')
# plt.plot(naxord_orer, ml_model.predict(naxord_orer))
# plt.show()
y_pred = ml_model.predict([[1]])
print(y_pred)
# print(help(ml_model.predict))