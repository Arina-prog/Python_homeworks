# Define a collection of color names, generate a new collection selecting
# only color name having more than 1 ‘o’ and print it
# Определите коллекцию названий цветов, сгенерируйте новую коллекцию,
# выбрав только название цвета, имеющее более 1 «о», и распечатайте ее.

color = ["red", "green", "blue", "orange", "yellow", "odofhdh"]

for i in color:
    count = 0
    for char in i:
        if char == "o":
            count += 1
            if count >= 2:
                print(i)



