# Create a class for representing employee with some attributes (name, position, salary, workdays (weekdays),
# completed tasks names) and behavior (change position, check if salary is higher than some threshold,
# find how many days salary works per week, find if employee works on some specific weekday), create several employees
# and perform actions, check how many employees are defined

# Создайте класс для представления сотрудника с некоторыми атрибутами (имя, должность, зарплата,
# рабочие дни (рабочие дни), названия выполненных задач) и поведением (измените должность, проверьте, не превышает
# ли зарплата некоторого порога, найдите, сколько дней зарплата работает в неделю, найдите если сотрудник работает в
# какой-то конкретный будний день),
# создайте несколько сотрудников и выполните действия, проверьте, сколько сотрудников определено

class Employee:
    """This is class Employee"""
    weekdays = []
    tasks_name = []

    def __init__(self, name, position, salary, weekdays, tasks_name):
        self.name = name
        self.position = position
        self.salary = salary
        self.weekdays = weekdays
        self.tasks_name = tasks_name

    def change_position(self, posit):
        self.position = posit

    def check_salary(self, salary):
        if self.salary > salary < 65000:
            self.salary = (self.salary - (self.salary - salary) * 0.21)

    def days_salary(self):
        print("days salary is ", len(self.weekdays))

    def show(self):
        print("employee name - " + self.name, "\n", "position - " + self.position, "\n",
              "check solory - " + str(self.salary),
              "\n", "weekdays - " + str(self.weekdays), "\n", "tasks name - " + str(self.tasks_name))


employ = Employee(name="Arman", position="Manager", salary=125000, weekdays=["erkushabti", "ereqshabti",
                                                                             "choreqshabti", "hingshabti", "urbat",
                                                                             "shabat"],
                  tasks_name=["hachaxordneri spasarkum", "hashvetvutyan kazmum"])
employ.change_position("administrator")
employ.check_salary(55000)
employ.show()
print("_________employee 1_______")
employee_1 = Employee("Karen", "teacher", 89000, ["erkushabti", "choreqshabti", "urbat", "shabat"],
                      ["dasi anckacum", "gortsnakan parapmunq", "arajadranqneri stugum"])
employee_1.show()
print("_________change position_______")
employee_1.change_position("administrator")
employee_1.show()
print("_________change salary_______")
employee_1.check_salary(55000)
employee_1.show()

print("_________change salary_______")
employee_1.days_salary()
employee_1.show()

print(employ.name)
