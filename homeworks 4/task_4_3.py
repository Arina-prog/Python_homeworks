# Define collection of numbers, get number at random position if it doesn’t exceed some inputed threshold value
# 3..Определите набор чисел, получите число в случайной
# позиции, если оно не превышает некоторого введенного порогового значения
import random
numbers = [12, 24, 26, 25, 48, 78, 895, -689, 1, 3595]
value = int(input("input threshhold value\n"))
index = random.randint(0, len(numbers))
if (numbers[index] > value):
    print("doesn’t exceed: " + str(numbers[index]))
else:
    print(" exceeding, index is :" + str(index))
