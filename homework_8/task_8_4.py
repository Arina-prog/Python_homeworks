import functools

numbers = [23, 56, 145, 25, 245, -25, 6.3,-4.56, -23]
result = functools.reduce(lambda num1, num2: num1 - num2, numbers)
print(result)