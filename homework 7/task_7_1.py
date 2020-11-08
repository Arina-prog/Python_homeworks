# Input 3 collections of numbers, calculate how many numbers are greater than 10
# for first, how many numbers are greater than 20 for second and how many numbers are greater
# than 30 for third collection
# (implement version without functions and version with functions)
#Введите 3 набора чисел, вычислите, сколько чисел больше 10 для первого, сколько чисел больше 20
# для второго и сколько чисел больше 30 для третьего набора (реализовать версию без функций и
# версию с функциями)
#
num_lis1 = [14, 9, 8, 25, 33, 7, 12, 5, 3, 42]
num_lis2 = [19, 34, 42, 20, 11, 6, 5, 16, 26, 19]
num_lis3 = [25, 24, 56, 125, 23, 10, 9, 8, 61, 3]
count1 = 0
count2 = 0
count3 = 0
for num in num_lis1:
    if num > 10:
        count1 += 1
for num in num_lis2:
    if num > 20:
        count2 += 1
for num in num_lis3:
    if num > 30:
        count3 += 1

print("in list 1 greater than 10 is {} numbers ".format(count1))
print("in list 2 greater than 20 is {} numbers ".format(count2))
print("in list 3 greater than 30 is {} numbers ".format(count3))


##########################################

def counter(arr, limit):

    count = 0
    for num in arr:
        if num > limit:
            count += 1
    return count
print(counter(num_lis1, 10))
print(counter(num_lis2, 20))
print(counter(num_lis3, 30))
