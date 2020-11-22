numbers_1 = [12, 24, 33, 66, 9, 8]
numbers_2 = [22, 14, 13, 26, 19, 6]

def get_square_sum(num_1, num_2):
    return(pow(num_1,2)+pow(num_2,2))
result = list(map(get_square_sum,numbers_1,numbers_2))
print(result)

results = list(map(lambda num1, num2: pow(num1,2)+pow(num2,2), numbers_1, numbers_2))
print(results)
#############
import functools


results = functools.reduce(lambda num_1, num_2: pow(num_1,2)+pow(num_2,2), numbers_1)
print(results)