# arr =  [1,6]
# print(len(arr))
#
# print(arr[-1])

arr = [5,8, 8]
print(len(arr))
print(arr[1])
print(arr[-2])

arr1 = [1,3,4,5,6,7,8,9]
print(arr1[-1:])

print(arr1[1:-1])
print(arr1[:len(arr1)//2])
print(arr1[1:5:2])
print(arr1[::3])
print(arr1[::-1])

print(arr1[::2])
print(arr1[1::2])

arr3 = arr + arr1
print(arr3)
arr = arr*2
print(arr)
arr[0] = [25,4]
print(arr)
matarr = [[1,9,1],[7,4,5]]

# print(dir(list))
# print(help(list.pop))



arr4 = [3, 67, 'yh', 55, '66']
arr4.append('p')
arr4.insert(3,44)
arr4.remove('yh')
arr4.pop(4)
arr4[2] = [1]*5
print(arr4)
print('yess') if 67 in arr4 else print('no')

# list1 = [1, 5, 7, 2, 7]
# for i in list1:
#     print(i)

# game_matrix = [['gold', 'bomb'], ['bomb', 'gold']]
# found = 0
# attempts = 3
#
# for i in range(attempts):
#     board_x = int(input('Write x coodinate:'))
#     board_y = int(input('Write y coodinate:'))
#     if game_matrix[board_x][board_y] == 'gold':
#         found += 1
#
# print('You won the game') if found == 2 else print('You lost')

print(list(range(7)))

matrix2 = [[1, 5, 8],
           [3, 4, 9],
           [5, 8, 77]]
col2 = [row[0]+6 for row in matrix2]
print(col2)

arr5 = [12, 51, 7, 9, 45, 30]
arr6 = [item for item in arr5 if item%3 == 0]
print(arr6)

diag = [matrix2[i][i] for i in range(len(matrix2))]
print(diag)

count_even = 0
for item in arr5:
    if item%2 == 0:
        count_even += 1

print(count_even)

for i in range(len(arr5)):
    if arr5[i]%2 == 0:
        print(i)


count = 0
for item in arr5:
    if item%5 == 0:
        count += 1

print(count)


divided_by5 = [i for i in range(len(arr5)) if arr5[i]%5 == 0]
print(divided_by5)
even_index = [i for i in divided_by5 if i%2 == 0]
print(len(even_index))

divided_by5.append(89)
print(divided_by5)
print(arr5[::3])
print(arr5[-1::2])