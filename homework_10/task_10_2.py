# Create a program that simultaneously adds and subtracts numbers collection and prints a message at the end.
# Создайте программу, которая одновременно складывает и вычитает набор чисел и печатает сообщение в конце.
import multiprocessing
import functools


def sum(numbers_1):
    summ = functools.reduce(lambda num_1, num_2: num_1 + num_2, numbers_1)
    print(summ)


def subtracts(numbers):
    result = functools.reduce(lambda num_1, num_2: num_1-num_2, numbers)
    print(result)


if __name__ == "__main__":
    numbers = range(5,500,2)
    proc_1 = multiprocessing.Process(target=sum, args=(numbers,))
    proc_2 = multiprocessing.Process(target=subtracts, args=(numbers,))
    proc_1.start()
    proc_2.start()

