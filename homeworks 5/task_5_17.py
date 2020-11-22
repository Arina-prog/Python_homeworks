# Create a collection of students with their scores and input them from console,
# remove students with score less than 40 and print final collection
# Создайте коллекцию учеников с их оценками и введите их с консоли,
# удалите учеников с оценкой менее 40 и распечатайте итоговую коллекцию
#
# student = {}
# count = 0
# stud_count = int(input("students  count:\n"))
#
# while(count < stud_count):
#     student[input("name")] = int(input("ball"))
#     count += 1
# print(student)
#
# students = {key: value for key, value in student.items() if value > 40}
# print(students)
#

students = {}
limit = 0
while limit <= 2:
    add_student = input('Enter Name of Student: ')
    students[add_student] = int(input('Add score: '))
    limit += 1

for key in students.keys():
    if students[key] > 40:
        # print(students[key])
        del students[key]
    # print(key)
    # print(students[key])


print(students)


