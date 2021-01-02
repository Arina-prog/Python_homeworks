# Create a variable storing integer, create 2 extra processes, one should add 3 to
# value 1000 times and transfer the result to another process which prints it.

# Создайте переменную, хранящую целое число, создайте 2 дополнительных процесса,
# нужно добавить 3 к значению 1000 раз и передать результат другому процессу, который его распечатает.

import multiprocessing


def put_number(number, queue):
    number = number+3*1000
    queue.put(number)
    print("end put_number")

def print_number(queue):
    while not (queue.empty()):
        print(queue.get())
    print("end print_number")


if __name__ == "__main__":
    number = int(input("mutqagreq tiv: "))
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=put_number, args=(number, queue,))
    p2 = multiprocessing.Process(target=print_number, args=(queue,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()