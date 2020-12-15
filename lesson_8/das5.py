v1 = 'this is my text'
v2 = 'my \n is'
v3 = 'it\'s my val'
v4 = 'this is with\t tab'
v5 = 'this is\\ double'
print('value 1 is: ', v1 )
print('value 2 is: ', v2 )
print('value 3 is: ', v3 )
print('value 4 is: ', v4 )
print('value 5 is: ', v5 )

arr = 'like array'
print('length: ', len(arr))
print('element number 2: ', arr[1])
print('last element: ', arr[-1])
print('second word: ', arr[5:])
print('even elements: ', arr[::2])

print(arr[::-1])
print(arr[:len(arr)//2])

print(arr*2)

num = 3
if num%2 == 0 or num > 5:
    print('zuyg e kam mec e 5 ')
elif num < 7 and num%3 == 0:
    print('poqr e 7 ic ev baj 3i')
else:
    print('voch arajin paymanner true voch 2rd')



for number in [1, 2, 3, 4, 5, 6, 7]:
    print(number)

#1. number = 1
#2. print(number)
#3. number = 2
#4. print(number)
#5. number = 3

print(list(range(1,8)))
for number in range(1, 8, 2):
    print(number)


# print(help(str.split))
#
print(dir(str))
#
# print(help(str.upper))
print(help(str.islower))

print('string'.upper())
print('hjbhiuUJNnj'.islower())

import re

print(dir(re))
