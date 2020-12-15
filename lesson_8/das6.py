weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# for day in weekdays:
#     print(day)

# print(seasons[-2])

# print(dir(tuple))
# print(help(tuple.index))


lesson_1_students = {'Sevak', 'Hrayr', 'Tigran', 'Tatevik'}
lesson_2_students = {'Sevak', 'Arina', 'Tatevik'}

print('Present in lesson 1 and 2: ', lesson_1_students&lesson_2_students)
print('Present in lesson 1 who are apsent in 2: ', lesson_1_students-lesson_2_students)
print('Present in lesson : ', lesson_1_students|lesson_2_students)

# numbers = {1, 12, 4, 55}
# numbers = [1, 12, 4, 55]
# sumary = 0
# for num in numbers:
#     if num%5 != 0:
#         sumary += num
#     else:
#         break
# print(sumary)


# print(numbers)
# print(list(numbers))
# sumary = 0
# for num in numbers:
#     if num%2 == 0:
#         sumary += num
#     else:
#         continue
# print(sumary)


# numbers = [2, 3, 4, 5, 2, 6]
# product = 1
# i = 0
#
# while numbers[i] < 5:
#     product = product * numbers[i]
#     i += 1
# print(product)

# print(dir(list))
# numbers = []
# count = 0
#
# while count < 2:
#     numbers.append(int(input('Write number: ')))
#     count += 1
# # print(numbers)
#
# i = 0
# # while numbers[i] < 10:
# #     print(numbers[i])
# #     i += 1
#
# for num in numbers:
#     if num > 4:
#         print(num)
#         break
# else:
#     print('there is no number that is true for condition')


number = 5
number2 = number

number = 2
# print(number2)

arr = [5, 5]
arr1 = arr

arr[0] = 7

print(arr1[0])
print(arr[0])