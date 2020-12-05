# Create 2 collections storing company employees,
# get number of employees working in both companies, get collection of employees with some name from both of groups,
# input several names and find if they work in one of companies, print results
# Создайте 2 коллекции, хранящие сотрудников компании, получите количество сотрудников,
# работающих в обеих компаниях, получите коллекцию сотрудников с некоторыми именами из обеих групп,
# введите несколько имен и найдите, работают ли они в одной из компаний, распечатайте результаты

##### set#####

set1 = {"Anna", "Denis", "Grig", "Alex", "Leo"}
set2 = {"Tigran", "Narek", "Grig", "Anna", "Jack", "Jhon"}
counts= len(set1)+len(set2)
unite = set1 | set2
print("unite", unite)
print(set1 & set2)
print(set1 - set2)
print("number of employees working in both companies:  ",counts)# new_group = []
count = 0
while(count < 5):
    names = input("input name:\n")
    if names in set1:
        print("yes in compony 1")
    else:
        print("No in company 1")
    if names in set2:
        print("yes in company 2")
    else:
        print("No in company 2")
    count += 1
