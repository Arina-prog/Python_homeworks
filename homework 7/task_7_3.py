# Define a collection of company employees (full name(‘Jack Smith’),
# position), calculate how many people with name ‘John’ work in company (create a function),
# calculate how many people have ‘Engineer’ position (create a function), print results
# Определите набор сотрудников компании (полное имя («Джек Смит»), должность), рассчитайте,
# сколько людей с именем «Джон» работает в компании
# (создайте функцию), подсчитайте, сколько человек занимает должность «Инженер» (создайте функциюю ),
# распечатать результаты:

employees = {"John Dck": "Builder", "Jach Smith": "Engineer", "John Braun": "Tractor driver",
             "Jonik Sckot": "Engineer", "Tom Smit": "Teacher",
             "John Dick": "Builder", "Jon Sckot": "Engineer"}


def counter(dictt):

    count = 0
    for emp in dictt:
        if "John" in emp:
            count += 1
    return count


def working(dictt):

    count = 0
    for emp in dictt.values():
        if "Engineer" in emp:
            count += 1
    return count

print(counter(employees))
print(working(employees))