#Input a collection of employee names with their salary,
# calculate average salary in organisation, get the employee with highest salary,
# get the employee with lowest salary print results.
# Введите коллекцию имен сотрудников с их зарплатой, вычислите среднюю зарплату в организации,
# получите сотрудника с самой высокой зарплатой, получите сотрудника с самой низкой зарплатой.

name_salary = {"Anna": 25600, "Denis": 35200, "Tom" : 56000, "Nik": 96000}
limit = int(input('Input a limit: '))
count = len(name_salary)
sum = 0
values = []
max = 0
min = 0
calc = 0
while calc < limit:
    name_salary[input('Add a name of employee: ')] = int(input('Add a salary: '))
    calc += 1
for sal in name_salary.values():
    values.append(sal)
    values.sort()
    sum += sal
average = sum/count
print("average is  " + str(average))
print("min is  " + str(values[0]))
print("max is  " + str(values[-1]))
