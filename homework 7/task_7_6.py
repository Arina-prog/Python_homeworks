# Create a calculator with different functions: 1) input numbers (one or more);
# 2) calculate different power for inputed numbers;
# 3) calculate how many numbers are greater than some specific number;
# 4) calculate how many numbers are even; 5) get number which power 3 is greater than 100
# Создайте калькулятор с различными функциями:
# 1) ввод чисел (одного или нескольких);
# 2) вычислить разную степень для введенных чисел;
# 3) посчитать, на сколько чисел больше определенного числа;
# 4) посчитайте, сколько чисел четное;
# 5) получить число, степень которого 3 больше 100

def power(arr, degri):
    lis = []
    for i in arr:
        result = pow(i, degri)
        lis.append(result)
    return lis


def greater(arr, const_num=25):
    lis = []
    for i in arr:
        result = i - const_num
        if result < 0:
            lis.append("no greater")
        else:
            lis.append(result)
    return lis


def power_3(arr):
    lis = []
    for i in arr:
        result = pow(i, 3)
        if result > 100:
            lis.append(i)
            lis.append(result)

    return lis


def even(arr):
    colc = 0
    for i in arr:
        if i % 2 == 0:
            colc += 1
    return colc


count = int(input("input count number:\n"))

colc = 0
const_num = 23


def inputer(colc, count):
    lis = []
    while(colc < count):
        num = int(input("number: "))
        lis.append(num)
        # degri = int(input("input degri\n"))
        colc += 1

    # return (power(lis, degri))

    # return (greater(lis, const_num))

    # return (power_3(lis))

    return (even(lis))


print(inputer(colc,count))