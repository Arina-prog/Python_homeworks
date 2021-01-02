# Define a shared collection of numbers, create 2 extra processes, one for adding 10
# to each element 5.000 times, another for subtracting 5 to each element 10.000 times, print result array.

# Определите общую коллекцию чисел, создайте 2 дополнительных процесса, один для добавления 10 к
# каждому элементу 5.000 раз, другой для вычитания 5 к каждому элементу 10.000 раз, распечатайте массив результатов.


#############################
# sahmanel 10000 bar amen barum hashvel "a" tareri qanakn,
# ka tveri havaqatsu 10000 , amen tvi gumarenq 5 bazmapatkenq 2-ov, gumarn tpel

# stextsel tveri colection ev stextsel 2 process ,a rajinn amen tvi +5, erkrordn stacvats ardyunqic gtnum e qani tiv ka
# >7-ic

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

#
# def number_a_s(word):
#     return word.count("a")
#
#
# if __name__ == "__main__":
#     words = ["barev"]*10000
#     pool = multiprocessing.Pool()
#     results = pool.map(number_a_s, words)
#     print(results)


#
# # balance = [5,10,25, 30]
# def plus(balance, amount, lock):
#
#     for i in range(1,100,2):
#         """procesn blok e anum"""
#         lock.acquire()
#         balance.value = balance.value + amount
#         """procesn blokic hanum  e """
#         lock.release()
#
#
# if __name__ == "__main__":
#         # balance = multiprocessing.Array('i')
#         lock = multiprocessing.Lock()
#         proc_1 = multiprocessing.Process(target=plus, args=([5,12,6,9,4], 10, lock))
#         # proc_2 = multiprocessing.Process(target=minus, args=(balance, 1, lock))
#         proc_1.start()
#         # proc_2.start()
#         proc_1.join()
#         # proc_2.join()
#         print("verjnakan balans = ", balance.value)
