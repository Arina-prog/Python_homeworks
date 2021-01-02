# Create a collection of numbers with size 10.000, create a function for multiplying each element by 5.
# Создайте набор чисел размером 10.000, создайте функцию для умножения каждого элемента на 5.

import multiprocessing
import time

def multipl(i):
    return i * 5

if __name__=="__main__":

    collection = range(10000)
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(multipl, collection)
    end_time = time.time()
    duration = end_time - start_time
    print(duration)
    print(result)