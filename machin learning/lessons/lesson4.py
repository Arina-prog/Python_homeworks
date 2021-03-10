import pandas as pd
import matplotlib.pyplot as plt

names = ["Arina", "Tatev", "Hrayr", "Robert"]
df = pd.DataFrame(names)
# print(df)
data = {"name": names, "salary": [150, 500, 256, 265], "gender": ['female', 'female', 'male', 'male'],
        "age": [25, 29, 35, 24]}
df_2 = pd.DataFrame(data, index=['admin', 'developer', 'manager', 'guard'])
# print(df_2)
# print(df_2[["name", "salary", "gender"]])
# print(df_2.loc[['admin', 'developer']])
# print(df_2.iloc[[0, 2]])
# print(df_2.sum(axis=1))
# print(df_2["salary"].sum())
# print(df_2["salary"].mean())
# df_2.plot()
# plt.show()
# df_2.plot.bar()
# plt.show()
df_3 = pd.read_csv("data_frame.csv")
# print(df_3)
# print(df_3.head())
# print(df_3.columns)
