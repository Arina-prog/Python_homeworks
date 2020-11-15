# Create a function with 2 parameters (function, number),
# call the function with some specific function described with lambda and integer inputed from console
# Создайте функцию с двумя параметрами (функция, число), вызовите функцию с некоторой конкретной функцией,
# описанной с помощью лямбда и целого числа, введенного с консоли
kx = int(input("input num:\n"))
def makeActions(k):
    act = []
    for i in range(k):
        act.append(lambda k, i=i: i**k)
    return act
    # sum = (lambda numb : numb*2)
    # return sum
print(makeActions(kx))