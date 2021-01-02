# Create 2 processes: 1. calculate sum of list of numbers and print it;
# 2. calculate count of even elements in list of numbers and print it.

# Создайте 2 процесса: 1. вычислите сумму списка чисел и распечатайте его;
# 2. Подсчитайте количество четных элементов  в списке чисел и распечатайте его

import multiprocessing
import functools


def sum(numbers_1):
    result = functools.reduce(lambda num_1, num_2: num_1 + num_2, numbers_1)
    print(result)


def even_count(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    numbers = range(120)
    proc_1 = multiprocessing.Process(target=sum, args=(numbers,))
    proc_2 = multiprocessing.Process(target=even_count, args=(numbers,))
    proc_1.start()
    proc_2.start()
    # proc_1.join()
    # proc_2.join()
