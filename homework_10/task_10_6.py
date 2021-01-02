# Define a collection of 5.000 numbers, create 3 extra processes, 1-st to multiply each element by 10,
# 2-nd to get from result by 1-st elements which can be divided by 3, 3-rd to see
# if sum of the result of 1-st is positive.
#
# Определите набор из 5.000 чисел, создайте 3 дополнительных процесса: 1-й, чтобы умножить каждый элемент
# на 10, 2-й, чтобы получить результат на 1-й элемент, который можно разделить на 3, 3-й, чтобы увидеть, есть ли сумма

import multiprocessing
import functools


def multiply(numbers):
    result = list(map(lambda number: number * 10, numbers))
    print(result)


def first_divided_3(numbers):
    for number in numbers:
        if number % 3 == 0:
            print(number)
            break


def sum_is_positiv(numbers):
    results = functools.reduce(lambda num_1, num_2: num_1 + num_2, numbers)
    if results > 0:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    numbers = multiprocessing.Array('i', range(1, 5000))
    p1 = multiprocessing.Process(target=multiply, args=(numbers,))
    p2 = multiprocessing.Process(target=first_divided_3, args=(numbers,))
    p3 = multiprocessing.Process(target=sum_is_positiv, args=(numbers,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()


