import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("diabetes.csv")
df.hist()
plt.show()