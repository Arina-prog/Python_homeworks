# Define a shared collection of numbers, create 2 extra processes, one for adding 10
# to each element 5.000 times, another for subtracting 5 to each element 10.000 times, print result array.

# Определите общую коллекцию чисел, создайте 2 дополнительных процесса, один для добавления 10 к
# каждому элементу 5.000 раз, другой для вычитания 5 к каждому элементу 10.000 раз, распечатайте массив результатов.


############version 1##############

import multiprocessing


def add(numbers):
    result = list(map(lambda number: number + 10 * 5000, numbers))
    print(result)


def to_each(numbers):
    result = list(map(lambda number: number - 5 * 10000, numbers))
    print(result)


if __name__ == "__main__":
    numbers = multiprocessing.Array('i', range(1000))
    p1 = multiprocessing.Process(target=add, args=(numbers,))
    p2 = multiprocessing.Process(target=to_each, args=(numbers, ))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
################version 2###############

# import multiprocessing
#
#
# def add(numbers, queue):
#     result = list(map(lambda number: number + 10 * 5000, numbers))
#     queue.put(result)
#     print(result)
#
#
# def to_each(queue):
#     new_list=[]
#     for number in (queue.get()):
#         number = number-5*10000
#         new_list.append(number)
#
#     print(new_list)
#
#
#
# if __name__ == "__main__":
#     queue = multiprocessing.Queue()
#     numbers = multiprocessing.Array('i', range(1000))
#     p1 = multiprocessing.Process(target=add, args=(numbers,queue))
#     p2 = multiprocessing.Process(target=to_each, args=(queue, ))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#
#
#
#


#############################
# sahmanel 10000 bar amen barum hashvel "a" tareri qanakn,
# ka tveri havaqatsu 10000 , amen tvi gumarenq 5 bazmapatkenq 2-ov, gumarn tpel

# stextsel tveri colection ev stextsel 2 process ,arajinn amen tvi +5, erkrordn stacvats ardyunqic gtnum e qani tiv ka
# >7-ic
"""
import multiprocessing


def add(numbers, queue):
    result = map(lambda tiv: tiv + 5, numbers)
    queue.put("p1 avartvel e")
    return result


def max_7(new_numbers, queue):
    while True:
        if not (queue.empty()):
            result = list(filter(lambda tiv: tiv > 7, new_numbers))
            count = len(result)
            print(count)
            break


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    numbers = multiprocessing.Array('i', range(10000))
    p1 = multiprocessing.Process(target=add, args=(numbers, queue))
    p2 = multiprocessing.Process(target=max_7, args=(numbers, queue))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

"""
