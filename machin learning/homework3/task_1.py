# Create numpy 2-dimensional array and perform different actions and calculations
# Создавайте numpy 2-мерный массив и выполняйте различные действия и вычисления

import numpy as np

# converting list to array
numbers = [11, -7, 9, 15, 34, 55]
numbers_np = np.array(numbers)
# print(numbers_np, "\n")

########### generating random array#########

random_numbers = np.random.rand(2, 2)
print(random_numbers, "\n")
#
#######################

rand_numbers = np.random.rand(2, 2) * 8
# print(rand_numbers, "\n")

#############
rand_num = np.random.rand(2, 2) + 1
# print(rand_num, "\n")

#################### oll 0 in array##########
matrix_zeros = np.zeros((2, 2))
# print(matrix_zeros, "\n")

#######################2*3 array, oll 4 in array##############
array_is_4 = np.full((2, 3), 4)
# print(array_is_4)

# print('numbers_np[0]  ', numbers_np[0], "\n")
# print('numbers_np[0:4] ', numbers_np[0:4], "\n")
# print('random_numbers[1, 1]', random_numbers[1, 1], "\n")
# print('random_numbers[1,:]', random_numbers[1, :], "\n")    #  ktpi 1-in toxn sax
# print('random_numbers[1, 0] ', random_numbers[1, 0], "\n")  #ktpi arajin toxi erkrord tarn @st indexi
print(random_numbers[0:, 1])

###########################

print("sort", numbers_np.sort())

print("transpose ", numbers_np.T)

print("reshape", numbers_np.reshape(-1, 1))

###############
numbers = np.append(numbers, 71)
# print(numbers, "\n")

######################

numbers = np.insert(numbers, 3, 20)
# print(numbers, "\n")

#########################
rand_numbers = np.delete(rand_numbers, 1, axis=1)
# print(rand_numbers)

#####################
rand_numbers = np.delete(rand_numbers, 1, axis=0)
# print(random_numbers)

########################
numbers = np.delete(numbers, 3)
# print(numbers)

################ max, min, sum, mean #########
matrix = [[16, 25],
          [9, 36]]

matrix_np = np.array(matrix)
print(matrix_np)
print("sum  ", matrix_np.sum())
print(matrix_np[1, 1])
print("min in array", matrix_np.min())
print("min in row", matrix_np.min(axis=0))
print("min in column", matrix_np.min(axis=1))
print("max in array", matrix_np.max())
print("max in row", matrix_np.max(axis=0))
print("max in column ", matrix_np.max(axis=1))
print("sum row", matrix_np.sum(axis=0))
print("sum column", matrix_np.sum(axis=1))
print("mean column", matrix_np.mean(axis=1))
print("mean row", matrix_np.mean(axis=0))
print("var ", np.var(matrix_np))
print("std ", np.std(matrix_np))
print("median ", np.median(matrix_np))

################ sqrt, sin, log, abs #####################
print("add  ", np.add(matrix_np, 5))
print("sqrt  ", np.sqrt(matrix_np))
print("sin  ", np.sin(matrix_np))
print("log ", np.log(matrix_np))
matrix_abs = [[-15, 35],
              [9, -36]]
print(np.abs(matrix_abs))
print(np.add(matrix_abs, matrix_np))
print(np.array_equal(matrix_np, matrix_np))
print(np.array_equal(matrix_np, matrix_abs))
print(np.ceil(random_numbers))
print(np.floor(random_numbers))
print(np.round(random_numbers))
# print(dir(np))
