# Create class Person with attributes (name, height that should be more than 30, sex that should be male or female)
# and some behavior, control the values, create objects and use them

# Создайте класс Person с атрибутами (имя, рост, который должен быть больше 30, пол, который должен быть мужской или
# женский) и некоторым поведением, контролировать значения, создавать объекты и использовать их

class Person:
    """This is class Person"""

    def __init__(self, name):
        self.name = name

    def age(self, age):
        if age > 30:
            self.age = age
        else:
            self.age = "tariqn chihamapatasxanum"
        # print(self.age)

    def sex(self, sex):
        if sex == "male" or sex == "female":
            self.sex = sex
        else:
            self.sex = "mutqagrel noric"
        # print(self.sex)

    def show(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
        print("Person sex = ", self.sex)


class Student(Person):
    def __init__(self, name, section):
        Person.__init__(self, name)
        self.section = section

    def showStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student sex = ", self.sex)
        print("Student section = ", self.section)


P = Person("A. Barsexyan")
P.sex("meal")
# P.sex("male")
P.age(32)
P.show()
print("-------------------------------")
S = Student("Alla", "Mathematics")
S.age(25)
S.sex("female")
S.showStudent()
