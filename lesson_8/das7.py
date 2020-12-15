# word = "hello"
# def greet(param):
#     """printing hello"""
#     print(param)
# greet(word)


# numbers = [1, 3, 4, 5]
# numbers2 = [1, 5, 6]
# def print_even(arr):
#     """printing even numbers"""
#     for num in arr:
#         if num % 2 == 0:
#             print(num)
#
# print_even(numbers)
# print_even(numbers2)
# print_even(arr=numbers)
# print_even(arr=numbers2)

# words = ["can", "students", "house", "car"]
# num = 4
#
# def get_words(arr, num):
#     result = []
#     for word in words:
#         if len(word) >= num:
#             result.append(word)
#     return result
#
# print(get_words(words, num))
#
# cars = {"BMW": 5, "opel": 7, "mersedess": 6}
# def get_cars(cars, limit):
#     result = []
#     for sits in cars.values():
#         if sits >= limit:
#             result.append(sits)
#     return result
#
#
# print(get_cars(cars, limit)

# def add(*numbers):
#     sum = 0
#     for num in numbers:
#          sum += num
#     print(sum)
# add(1)
# add(3, 4)
# add(3, 4, 5, 9)
#

#
# def perform_action(number1, number2, act):
#     value = act(number1, number2)
#     print(value)
#
# def mult(num1, num2):
#     return num1 * num2
#
# def add (val1, val2):
#     return val1 + val2
#
# perform_action(1, 5, mult)
# perform_action(7, 8, add)
# add = lambda val1, val2: val1 + val2
# perform_action(5, 4, lambda val1, val2: val1 + val2)

import os

f = open(r"C:\Users\Ser-Ar\Desktop\text.txt", "w")
# f = open("C:\\Users\\Ser-Ar\\Desktop\\text.txt", "w")
# f = open("C:/Users/Ser-Ar/Desktop/text.txt", "w")
# f.write("Hello")
f.write("")
f.close()

print(dir(os))
