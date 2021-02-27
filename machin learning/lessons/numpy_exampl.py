import numpy as np

# numbers = [10, 24, 63, 24]
# # converting list to array
# numbers_np = np.array(numbers)
# print(numbers)
# print(numbers_np)
# # generating random array
# random_number = np.random.rand(3, 6)
# print(random_number)
# random_numbers = np.random.rand(3, 6) * 5
# print(random_numbers)
# random_num = np.random.rand(3, 6) * 5 + 1
# print(random_num)
# # creating array in zero
#
# zero = np.zeros((3, 3))
# print(zero)
#
# print(numbers_np[0])
# print(numbers_np[0:4])
# print(random_number[1, 0])
# print(random_number[1, :])
# print(random_number[1, 2])
#
# random_number = np.append(random_number, 10)
# print(random_number)
# random_numbers = np.insert(random_numbers, 3, 20)
# print(random_numbers)
# random_num = np.delete(random_num, 1, axis=1)
# numbers = np.delete(numbers, 1)
# print(numbers)

"""Convert from list to ndarray
numpy_array = np.array(original_list)
Generating random ndarray
rarray = np.random.rand(2,2) # 2x2 array of number from 0 to 1
rarray = np.random.rand(3,2)*15 # 3x2 array of number from 0 to 15
Creating array of zeros
Indexing
array[1]
array[2,3] #[2][3]
array[2:5] 
array[1:3,5]
array[:,5] = 6 # assign 6 to 6th column
np.append(array,values) #append values to end of array.
np.insert(array, 3, values)  #insert values into array before index 3
np.delete(array, 4, axis=0) #delete row on index 4 of array
np.delete(array, 5, axis=1) #delete column on index 5 of array
np.mean(array,axis=0) will return mean along specific axis (0 or 1)
array.sum() will return the sum of the array
array.min()will return the minimum value of the array
array.max(axis=0)will return the maximum value of specific axis
np.var(array)will return the variance of the array
np.std(array,axis=1)will return the standard deviation of specific axis
array.corrcoef()will return the correlation coefficient of the array
numpy.median(array) will return the median of the array elements"""

matrix = [[10, 25, 36],
          [56, 34, 45]]

matrix_np = np.array(matrix)
print(matrix_np)
print(matrix_np.sum())
print(matrix_np[1, 1])
print(matrix_np.min())
print(matrix_np.min(axis=0))
# axis=0 syun, axis =1 tox
print(matrix_np.min(axis=1))
print(matrix_np.max())
print(matrix_np.max(axis=0))
print(matrix_np.max(axis=1))
print(matrix_np.sum(axis=0))
print(matrix_np.sum(axis=1))
print(matrix_np.mean(axis=1))
# mijin tvabanakan

"""np.add(array ,1) will add 1 to each element in the array and np.add(array1,array2) will add array 2 to array 1. The same is true to np.subtract(), np.multiply(), np.divide() and np.power() — all these commands would work in exactly the same way as described above.

np.sqrt(array) will return the square root of each element in the array
np.sin(array) will return the sine of each element in the array
np.log(array) will return the natural log of each element in the array
np.abs(arr) will return the absolute value of each element in the array
np.array_equal(arr1,arr2) will return True if the arrays have the same elements and shape"""
matrixis = [[10, 23, 25], [7, 5, 9]]
print(np.sqrt(matrix_np))
print(np.sin(matrix_np))
print(np.log(matrix_np))
print(np.array_equal(matrix_np, matrixis))
print(dir(np))
