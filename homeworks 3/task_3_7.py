# Generate a random number from 1 to 100 and check if the number is greater than 15 and less than 36
# # 7...generacnel 1-100 mijakayqi tiv  ev stugel ardyoq 15-ic mets e ev 36ic poqr te voch

import random

rand_number = random.randint(1, 100)
if(rand_number > 15 and rand_number < 36):
    print("yes")
else:
    print("no")
print(rand_number)