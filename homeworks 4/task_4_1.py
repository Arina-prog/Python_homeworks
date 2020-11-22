# *Define a collection of weekdays, print following: first 5 week days, total days number, last 2 days, odd days
#1... Определите набор дней недели, напечатайте следующее:
# первые 5 дней недели, общее количество дней, последние 2 дня, нечетные дни

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday:", "Sunday"]
count = 0
working_days = []
odd_days = []
for i in week:
    if (count < 5):
        working_days.append(week[count])
    if count % 2 != 0:
        odd_days.append(week[count])
    count += 1
print(working_days)
print(len(week))
print(week[5:])
print(week[:5])
print(odd_days)

#########version 2############################
working_days = []
odd_days = []
for i in week:
    if week.index(i) % 2 !=0:
        odd_days.append(i)


print(len(week))
print(week[5:])
print(week[:5])
print(odd_days)
