# Define a collection of pets, that stores types of pet and its name,
# find how many pets have name Johny and print the number
#Определите коллекцию домашних животных, в которой хранятся типы питомца и его имя,
# найдите, сколько домашних животных имеют имя Джонни, и распечатайте номер

pets = {"pig": "Johny", "cat": "Murzik", "dog": "Johny", " mouse": "Jery"}
count = 0
for pet in pets.values():
    if pet == "Johny":
        count += 1
print(count)