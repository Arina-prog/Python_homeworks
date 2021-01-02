# Create a collection of country names with their temperature, simultaneously increment temperature of
# cities which name starts with ‘T’ or ‘I’, subtract by 5 temperature of
# countries which name starts with ‘A’ or ‘R’, print the result

# Создайте коллекцию названий стран с их температурой, одновременно увеличивая температуру городов, названия которых
# начинаются с «T» или «I», вычитайте на 5 температуру стран, названия которых начинаются с
# «A» или «R», распечатайте результат
#
# import multiprocessing
#
#
# def temp_increm(colection, lock):
#     for key in colection.keys():
#         if key[0] == "T" or key[0] == "I":
#             lock.acquire()
#             colection[key] += 10
#             lock.release()
#     print(colection)
#
#
#
# def temp_subtract(colection, lock):
#     for key in colection.keys():
#         if key[0] == "A" or key[0] == "R":
#             lock.acquire()
#             colection[key] -= 5
#             lock.release()
#     print(colection)
#
#
# if __name__ == "__main__":
#     colection = {"Chikago": 18, "Tokio": 25, "Ijevan": 6, "Rastov": 13, "Riga": (-6), "Anapa": 8}
#     lock = multiprocessing.Lock()
#     p1 = multiprocessing.Process(target=temp_increm, args=(colection, lock))
#     p2 = multiprocessing.Process(target=temp_subtract, args=(colection,lock))
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()


##################version 2##################
import multiprocessing


def temp_increm(colection, queue):
    for key in colection.keys():
        if key[0] == "T" or key[0] == "I":
            colection[key] += 10
            queue.put(colection)
    # print(colection)



def temp_subtract(queue):
    dict_1 =queue.get()
    for key in dict_1.keys():
        if key[0] == "A" or key[0] == "R":
            dict_1[key] -= 5
    print(dict_1)


if __name__ == "__main__":
    colection = {"Chikago": 18, "Tokio": 25, "Ijevan": 6, "Rastov": 13, "Riga": (-6), "Anapa": 8}
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=temp_increm, args=(colection, queue))
    p2 = multiprocessing.Process(target=temp_subtract, args=(queue,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
