import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("diabetes.csv")
plt.matshow(df.corr())
plt.xticks(range(df.shape[1]), df.columns, fontsize=12, rotation=90)
plt.yticks(range(df.shape[1]), df.columns, fontsize=12)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=12)
plt.title('Correlation Matrix')
plt.show()