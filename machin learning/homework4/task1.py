import pandas as pd
import matplotlib.pyplot as plt

fruits = ["banana", "apple", "chary", "orange"]
df_frits = pd.DataFrame(fruits)
df_frits1 = pd.DataFrame(data=fruits)
# print(df_frits, "\n")
# print(df_frits1)

###########
sale = {"name": fruits, "price": [650, 450, 1200, 750], "kg": [53, 150, 26, 70]}
df_sale = pd.DataFrame(sale)
df_sales = pd.DataFrame(sale, index=["stend 1", "stend 2", "stend 3", "stend 4"])
# print(df_sale, "\n")
print(df_sales, "\n")
# print(df_sales.dtypes)

###########
# print(df_sale["name"], "\n")
# print(df_sale["price"], "\n")
# print(df_sale["price"]+260, "\n")
# print(df_sales[["name", "price"]], "\n")
############
# print(df_sales.loc["stend 2"], "\n")
# print(df_sales.loc[["stend 1", "stend 4"]], "\n")
############
# print(df_sales.iloc[3], "\n")
# print(df_sales.iloc[[1, 0, 3]], "\n")
###########
# print(df_sales.sum(axis=1), "\n")
# print(df_sales.sum(axis=0), "\n")
######
# print(df_sales["price"].sum(), "\n")
# print(df_sales["kg"].mean())
# print(df_sales["price"].mean())
############
df_sales.plot()
# plt.show()
df_sales.plot.bar()
# plt.show()
########
# print(df_sales["price"].div(10))
# print(df_sales["price"].rdiv(2))
print(df_sales.append(df_frits))
print(df_sales.any())
# print(help(df_sales))
print(df_sales.count())