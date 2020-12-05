# Define a collection of color names, generate a new collection selecting
# only color name having more than 1 ‘o’ and print it
# Определите коллекцию названий цветов, сгенерируйте новую коллекцию,
# выбрав только название цвета, имеющее более 1 «о», и распечатайте ее.

color = ["red", "green", "blue", "borow",  "orange", "yellow", "odofhdh"]
new_color = []
for char in color:
    if char.count('o')>1:
        new_color.append(char)
print(new_color)

#############################
color = ["red", "green", "blue", "borow",  "orange", "yellow", "odofhdh"]
new_color = []
for i in color:
    count = 0
    for char in i:
        if char == "o":
            count += 1
            if count >= 2:
                print(i)
