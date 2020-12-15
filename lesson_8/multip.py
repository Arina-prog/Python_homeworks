import multiprocessing

"""
def print_word(word):
    while True:
        print(word)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_word, args=("hello",))
    p2 = multiprocessing.Process(target=print_word, args=("barev",))
    p1.start()
    p2.start()
"""

#
# def act(numbers):
#     numbers[0] = 55
#     print(numbers)
#
#
# if __name__ == "__main__":
#     numbers = [2, 3, 5, 8]
#     p1 = multiprocessing.Process(target=act, args=(numbers,))
#     p1.start()
#     p1.join()
#     print(list(numbers))
#
# if __name__ == "__main__":
#     # numbers = [2, 3, 5, 8]
#     numbers = multiprocessing.Array('i',[2,7,4,8])
#     p1 = multiprocessing.Process(target=act, args=(numbers,))
#     p1.start()
#     p1.join()
#     print(list(numbers))

# if __name__ == "__main__":
#     manager = Manager()
#     d = manager.dict()
#     I = manager.list(range(10))
#
#     p = Process(target=f, args=(numbers,))
#     p1.start()
#     p1.join()
#     print(list(numbers))

def put_numbers(queue):
    for i in range(10):
        queue.put(i)

def print_numbers(queue):
    while not(queue.empty()):
        print(queue.get())
    print("chka")

if __name__=="__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=put_numbers, args=(queue,))
    p2 = multiprocessing.Process(target=print_numbers, args=(queue,))
    p1.start()
    p2.join()
    p2.start()
    p1.join()

