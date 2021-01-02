# Input a collection of numbers, create 3 extra processes, one for adding 2 to each element, 2-nd for
# calculating number of positive elements in result of 1-st, 3-rd to
# calculate power 5 of result of 2-nd and print the result.

# Введите набор чисел, создайте 3 дополнительных процесса, один для добавления 2 к каждому элементу,
# 2-й для вычисления количества положительных элементов в результате 1-го, 3-й для
# вычисления степени 5 результата 2-го и выведите


import multiprocessing


def add(numbers, queue):
    result = list(map(lambda number: number + 2, numbers))
    queue.put(result)
    print(result)


def positiv_el_numbers(queue):
    count = 0
    for number in (queue.get()):
        if number > 0:
            count += 1
    queue.put(count)
    print(count)


def power(queue):
    while not (queue.empty()):
        result = (queue.get()) ** 5
        print(result)
        break


if __name__ == "__main__":
    numbers = multiprocessing.Array('i', range(-120, 100, 3))
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=add, args=(numbers, queue,))
    p2 = multiprocessing.Process(target=positiv_el_numbers, args=(queue,))
    p3 = multiprocessing.Process(target=power, args=(queue,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
