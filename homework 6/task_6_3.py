# Create 2 collections storing company employees,
# get number of employees working in both companies, get collection of employees with some name from both of groups,
# input several names and find if they work in one of companies, print results
# Создайте 2 коллекции, хранящие сотрудников компании, получите количество сотрудников,
# работающих в обеих компаниях, получите коллекцию сотрудников с некоторыми именами из обеих групп,
# введите несколько имен и найдите, работают ли они в одной из компаний, распечатайте результаты



company_1 = ["Anna", "Denis", "Grig", "Alex", "Leo"]
company_2 = ["Tigran", "Narek", "Grig", "Anna", "Jack", "Jhon"]
grups = company_1 +company_2
print("collection of employees with some name from both of groups: \n" + str(grups))
new_group = []
index = 0
# for name in grups:
for name in company_1:
    if index % 2 == 0:
        new_group.append(name)
    index += 1
for name in company_2:
    if index % 2 == 0:
        new_group.append(name)
    index += 1
print(new_group)
count = 0
while(count < 5):
    names = input("input name:\n")
    if names in company_1:
        print("yes in compony 1")
    else:
        print("No in company 1")
    if names in company_2:
        print("yes in company 2")
    else:
        print("No in company 2")
    count += 1
