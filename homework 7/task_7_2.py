# Input a collection of numbers, calculate how many numbers are positive and dividable by 6 (create a function),
# generate a new collection of odd numbers (create a function), print results
# Введите набор чисел, вычислите, сколько чисел положительные и делятся на 6 (создайте функцию),
# сгенерируйте новую коллекцию нечетных чисел (создайте функцию), распечатайте результаты

numbers = [12, 23, -56, -48, 63, 24, 154, 13, -15,  59, 45, 36]
odd_nums = []


def divisible(arr):

    count = 0
    for num in arr:
        if num > 0 and num % 6 == 0:
            count += 1
            print(num)
    return count


def odd_num(arr):

    for num in arr:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums


print(divisible(numbers))
print(odd_num(numbers))

