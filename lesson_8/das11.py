import multiprocessing
import time


# def plus(balance, amount, lock):
#     for i in range(10000):
#         """procesn blok e anum"""
#         lock.acquire()
#         balance.value = balance.value + amount
#         """procesn blokic hanum  e """
#         lock.release()
#
#
# def minus(balance, amount, lock):
#     for i in range(10000):
#         lock.acquire()
#         balance.value = balance.value - amount
#         lock.release()


# if __name__ == "__main__":
#     balance = multiprocessing.Value('i', 125)
#
#     proc_1 = multiprocessing.Process(target=plus, args=(balance, 1))
#     proc_2 = multiprocessing.Process(target=minus, args=(balance, 1))
#     proc_1.start()
#     proc_2.start()
#     proc_1.join()
#     proc_2.join()
#     print("verjnakan balans = ", balance.value)

def add(i):
    return i + 5


if __name__ == "__main__":
    #     balance = multiprocessing.Value('i', 100)
    #     lock = multiprocessing.Lock()
    #     proc_1 = multiprocessing.Process(target=plus, args=(balance, 1, lock))
    #     proc_2 = multiprocessing.Process(target=minus, args=(balance, 1, lock))
    #     proc_1.start()
    #     proc_2.start()
    #     proc_1.join()
    #     proc_2.join()
    #     print("verjnakan balans = ", balance.value)

    collection = range(10000)
    start_time = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(add, collection)
    end_time = time.time()
    duration = end_time - start_time
    print(duration)
    print(result)

collection = range(10000)
start_time = time.time()
result = list(map(add, collection))
end_time = time.time()
duration = end_time - start_time
print(duration)
print(result)
