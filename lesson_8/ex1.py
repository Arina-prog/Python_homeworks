# # nnumber = [12, 36, 8, 9]
# #
# #
# # def multiply_by_3(num):
# #     return num*3
# #
# #

# # result = list(map(multiply_by_3, nnumber))
# # print(result)
#
# ##############################
#
# words_1 = ['cat', 'dog', 'milk', 'bag']
# words_2 = ['loom', 'drop', 'milkiway', 'big_bag']
#
# def concat(word1, word2):
#     return word1+word2
#
# result1 = list(map(lambda words_1, words_2: words_1 + words_2, words_1, words_2 ))
# result = list(map(concat, words_1, words_2))
# print(result)
# print("lambda", result1)
#
# numbers = [2, 21, 36, 5, 6]
# result22 = list(filter(lambda a: 3 < a < 10, numbers))
# filt = list(filter(lambda x: x % 2 == 0, numbers))
# print(filt)
# print(result22)
#
# def is_between_3_10(x):
#     # return 3<x<10
#     if 3 < x < 10:
#         return True
#     else:
#         return False
#
# import functools
#
# result33 = functools.reduce(lambda x,y: x + y,range(1,10))
# print("reduce", result)
#
#
import functools

words_1 = ['asdsa', 'adfdg', 'adssffgf', 'adfdgh']
result = functools.reduce(lambda word_1, word_2: word_1 + word_2, words_1)
print(result)

