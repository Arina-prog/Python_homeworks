import matplotlib.pyplot as plt

fig = plt.figure()
# ax_1 = fig.add_subplot(121)
ax_1 = fig.add_subplot(221)
# ax_2 = fig.add_subplot(122)
ax_2 = fig.add_subplot(222)
ax_3 = fig.add_subplot(223)
x = [4, 8, 12]
y = [2, 5, 9]
x2 = [1, 3, 2.6, 7]
y2 = [2, 4, 1.5, 8]
ax_1.title.set_text("graf 1")
ax_1.plot(x, y, "b--")
# ax_2.plot(x2, y2, "g")
ax_2.title.set_text("graf 2")
ax_2.scatter(x2, y2)
# ax_3.plot([4, 5, 2, 1], [2, 4, 3, 2])
ax_3.title.set_text("graf 3")
ax_3.bar([4, 5, 2, 1], [2, 4, 3, 2])
plt.show()
