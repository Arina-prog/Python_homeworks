import pandas as pd
import matplotlib.pyplot as plt

# plt.plot([1, 3, 7, 9, 12]) #y
# plt.plot([4, 8, 10])
x = [2, 4, 10]
y = [7, 9, 11]
# plt.plot(x, y)
# plt.plot(x, y, 'bo')
# plt.plot(x, y, 'b-')
# plt.plot(x, y, 'b+')
# plt.plot(x, y, 'b^--')
plt.plot(x, y, 'b^--')
# plt.plot(x, y, 'b+-')
# plt.plot(x, y, 'b+', color="red")
x_2 = [2, 4, 6, 8, 10]
y_2 = [3, 5, 7, 9, 11]
plt.plot(x_2, y_2, "g+-")
# plt.bar(x,y)
# plt.barh(x,y)
plt.scatter([1, 2, 6], [4, 2.5, 3.6], color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(2, 5)
plt.show()
# print(help(plt.plot))
# print(dir(plt))
# print(help(plt.bar))
