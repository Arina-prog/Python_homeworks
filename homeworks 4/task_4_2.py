# Define a collection of colors, add a color from console, print total colors number, print colors on even positions
# 2... Определите набор цветов, добавьте цвет из консоли,
# # распечатайте общее количество цветов, распечатайте цвета на четных позициях

color = ["black", "white", "red"]
color.append(input("input color\n"))
length = len(color)
even_pos = []
index = 0
for i in color:
    if (index % 2 == 0):
    # if ( index > 0 and index % 2 == 0):
        even_pos.append(color[index])
    index += 1
print(color)
print(length)
print(even_pos)
######################vers 2##############
even_pos = []
for i in color:
    if color.index(i) % 2 == 0:
        even_pos.append(i)

print(color)
print(length)
print(even_pos)