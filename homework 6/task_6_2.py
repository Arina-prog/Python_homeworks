# Create a collection for storing unique book names, add some of them from console and print results
# Создайте коллекцию для хранения уникальных названий книг,
# добавьте некоторые из них из консоли и распечатайте результаты

#####set####

book = {"Margo taguhin", "Musa leran 40 or@", "Vardananq"}
count = int(input("input book name count>3: \n"))
# book.append(input('Write your favorite Book name: '))
while(len(book) < count):
    book.add(input("input book name:\n "))
print(book)

